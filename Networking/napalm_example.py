import napalm
import json
import copy
from netmiko_connect import cisco_sandbox_type

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


IOS = 'ios'
IOSXR = 'ios-xr'
NXOS = 'nxos' # for napalm API
NXOS_SSH = 'nxos_ssh' # For connecting via napalm ssh

devices = copy.deepcopy(cisco_sandbox_type)

# Make a copy of NXOS for both NXOSAPI and NXOSSSH connections
devices[NXOS_SSH] = copy.deepcopy(devices[NXOS])

#print(devices,end = '\n')

for device_type, device in devices.items():
    print(f'\n------------connecting to {device_type} : {device["hostname"]}---------')

    if device_type == IOSXR:
        driver  = napalm.get_network_driver('ios')
    else:
        driver = napalm.get_network_driver(device_type)
    if device_type == NXOS:
        napalm_device = driver(
            hostname=device["hostname"],
            username=device["username"],
            password=device["password"]
        )
    else:
        napalm_device = driver(
            hostname=device["hostname"],
            username=device["username"],
            password=device["password"],
            optional_args={
                "port": 22,
                #"port":device["port"]
            }
        )

    napalm_device.open()

    print("\n------Get Facts-------")
    try:
        print(json.dumps(napalm_device.get_facts(), sort_keys=True, indent=4))
    except IndexError as e:
        print("There was an indexing error ", e)

    print("\n------Get Interfaces-------")
    print(json.dumps(napalm_device.get_interfaces(), sort_keys=True, indent=4))

    print("\n------vlans-------")
    try:
        print(json.dumps(napalm_device.get_vlans(), sort_keys=True, indent=4))
    except NotImplementedError as e:
        print(f"oops, looks like this isn't implemented for {device['hostname']}, error: {e}")

    print("\n------snmp-------")
    print(json.dumps(napalm_device.get_snmp_information(), sort_keys=True, indent=4))


    print("\n------Interface counters--------")
    try:
        print(json.dumps(napalm_device.get_interfaces_counters(),sort_keys=True,indent=4))
    except (ValueError, NotImplementedError)  as e:
        print(f"oops, looks like this isn't implemented for {device['hostname']}, error: {e}")


    print("\n---------Environment---------")
    try:
        print(json.dumps(napalm_device.get_environment(),sort_keys=True,indent=4))
    except (KeyError, IOError, UnboundLocalError) as e:
        print(f"oops, looks like this isn't implemented for {device['hostname']}, error: {e}")

    napalm_device.close()










