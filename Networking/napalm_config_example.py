import copy
from os import write

from netmiko_connect import cisco_sandbox_type
import napalm
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

    print(f"------connect to                   device {device['hostname']}, type={device_type}")
    napalm_device.open()

    print(f"------get configuration for        device {device['hostname']}, type={device_type}")
    # Note: NXOS requires a special method of napalm to get the configuration
    if device_type == NXOS or device_type == NXOS_SSH:
        configForCompare = napalm_device._get_checkpoint_file()
    else:
        configForCompare = napalm_device.get_config()["running"]

    with open(f"cisco.{device_type}.config", "w") as configOut:
        configOut.write(configForCompare)

    print(f"------loading configuration for    device {device['hostname']}, type={device_type}")
    napalm_device.load_replace_candidate(filename=f"cisco.{device_type}.config")
    print(f"------comparing configuration for  device {device['hostname']}, type={device_type}")
    diff = napalm_device.compare_config()
    print(f"------diff in config for           device {device['hostname']}, type={device_type}")
    print("diff:\n", diff)

    napalm_device.close()
