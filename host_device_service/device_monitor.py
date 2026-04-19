from datetime import datetime, timedelta
from time import sleep
import requests
import napalm
from napalm.base.exceptions import NapalmException
import yaml
import time
import socket
import re


MONITOR_INTERVAL = 15
DISCOVERY_INTERVAL = 300


def get_version(device, facts):
    if device["os"] == "iosxe":

        re_version_pattern = r"Version (.*),"
        version_match = re.search(re_version_pattern, facts["os_version"])
        if version_match:
            return version_match.group(1)
        else:
            return "--"

    return facts["os_version"]


def get_device_facts(device):

    try:
        if device['os'] == 'ios' or device['os'] == 'iosxe':
            driver = napalm.get_network_driver('ios')
        elif device['os'] == 'nxos-ssh':
            driver = napalm.get_network_driver('nxos-ssh')
        elif device['os'] == 'nxos':
            driver = napalm.get_network_driver('nxos')
        else:
            driver = napalm.get_network_driver(device['os'])

        napalm_device = driver(
            hostname = device['hostname'],
            username= device['username'],
            password= device['password'],
            optional_args={"port" : device["ssh_port"]}
        )
        napalm_device.open()
        time_start = time.time()
        facts = napalm_device.get_facts()
        response_time = time.time() - time_start

        device['os-version'] = get_version(device, facts)
        device['model'] = facts['model']
        device["availability"] = True
        device["response_time"] = response_time
        device["last_heard"] = str(datetime.now())[:-3]

    except NapalmException as e:
        print(f"  !!! Failed to get facts for device {device['name']}: {e}")
        device["availability"] = False


def get_devices():
    print("\n\n----> Retrieving devices ...", end="")
    resp = requests.get("http://127.0.0.1:5000/devices")
    if resp.status_code != 200:
        print(f" !!!  Failed to retrieve Devices from server: {resp.reason}")
        return {}
    print("Devices successfully retrieved")
    return resp.json()


def update_devices(device):
    print(f".......Updating the Device info using REST API: {device['name']}", end="")
    rsp = requests.put("http://127.0.0.1:5000/devices", params={"name": device['name']}, json=device)
    if rsp.status_code != 204:
        print(
            f"{str(datetime.now())[:-3]}: Error posting to /devices, response: {rsp.status_code}, {rsp.content}"
        )
        print(f" !!!  Unsuccessful attempt to update device status via REST API: {device['name']}")
    else:
        print(f" Successfully updated device status via REST API: {device['name']}")


def discovery():
    # 'discovery' of devices means reading them from the devices.yaml file
    print(
        "\n\n----- Discovery devices from inventory ---------------------"
    )

    with open("devies.yaml", "r") as yaml_in:
        yaml_devies = yaml_in.read()
        devices = yaml.safe_load(yaml_devies)

    existing_devices = get_devices()

    for device in devices:
        try:
            device['ip_address'] = socket.gethostbyname(hostname)
        except (socket.error, socket.gaierror):
            print(f"  !!! Error attempting to get ip address for device {device['hostname']}: {e}")
            device["ip_address"] = ""

        if device['name'] in existing_devices:
            existing_devices[device['name']]['ip_address'] = device['ip_address']
            device = existing_devices[device['name']]
        else:
            device['availability'] = False
            device['response_time'] = 0.0
            device['model'] = ""
            device['os_version'] = ""
            device['last_heard'] = ""

        update_devices(device)


def main():

    last_discovery = datetime.now()-timedelta(days=1)

    if (datetime.now() - last_discovery).total_seconds() > DISCOVERY_INTERVAL:
        discovery()
        last_discovery = datetime.now()

    devices = get_devices()
    for device in devices.values():
        get_device_facts(device)
        update_devices(device)
    sleep(MONITOR_INTERVAL)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting hot-monitor")
        exit()
