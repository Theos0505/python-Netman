# This utils file is for an example purpose of modules in python
# Multiple devices are created in this file and returned


import string
from random import choice


def creat_devices(num_device=2, num_subnets=1):  # Default parameters if no value is passed

    created_devices = list()

    for subnet_index in range(num_subnets):

        for device_index in range(1, num_device + 1):

            devices = dict()

            # Giving different name to device
            devices['name'] = (
                    choice(['r2', 'r3', 'r4', 'r5', 'r6']) + choice(['L', 'U']) + choice(string.ascii_letters))

            # Giving different vendor names

            devices['vendor'] = choice(["cisco", "jupitor", "arista"])

            if devices['vendor'] == "cisco":
                devices['os'] = choice(["ios", "iosxe", "iosxr", "nexus"])
                devices['version'] = choice(["12.1.(T).04", "14.07x", "8.12(S).810", "20.45"])
            elif devices['vendor'] == "jupitor":
                devices['os'] = choice(["junos"])
                devices['version'] = choice(["J6.23.1", "8.43.12", "6.45", "6.03"])
            elif devices['vendor'] == "arista":
                devices['os'] = choice(["eos"])
                devices['version'] = choice(["2.45", "2.55", "2.92.145", "3.01"])
            devices['ip'] = '10.0.' + str(subnet_index) + "." + str(device_index)

            created_devices.append(devices)

    return created_devices


def create_network(num_devices=1, num_subnets=1):
    devices = creat_devices(num_devices, num_subnets)
    network = dict()
    network['subnet'] = dict()

    for device in devices:
        subnet_address_bytes = device['ip'].split('.')
        subnet_address_bytes[3] = '0'
        subnet_address = ".".join(subnet_address_bytes)
        if subnet_address not in network['subnet']:
            network['subnet'][subnet_address] = dict()
            network['subnet'][subnet_address]['devices'] = list()
        network['subnet'][subnet_address]['devices'].append(device)

        interface = list()
        for index in range(choice([2, 4, 8])):
            interfaces = {
                "name" :'g 0/0/' + str(index),
                "speed" : choice(['10', '100', '1000'])
            }
            interface.append(interfaces)
        device['interfaces'] = interface
    return network

