from tabulate import tabulate
import string
from random import choice
from operator import itemgetter
from pprint import pprint


device = list()

for i in range(10):
    devices = dict()

    # Giving different name to device
    devices['name'] = (choice(['r2', 'r3', 'r4', 'r5', 'r6']) + choice(['L', 'U']) + choice(string.ascii_letters))

    # Giving different vendor names

    devices['vendor'] = choice(["cisco", "jupitor", "arista"])

    if devices['vendor'] == "cisco":
        devices['os'] = choice(["ios", "iosxe", "iosxr", "nexus"])
        devices['version'] = choice(["12.1.(T).04", "14.07x", "8.12(S).810", "20.45"])
    elif devices['vendor'] == "jupitor":
        devices['os'] = choice("junos")
        devices['version'] = choice(["J6.23.1", "8.43.12", "6.45", "6.03"])
    elif devices['vendor'] == "arista":
        devices['os'] = choice("eos")
        devices['version'] = choice(["2.45", "2.55", "2.92.145", "3.01"])
    devices['ip'] = '10.0.0.' + str(i)

    print()
    # Formated print

    for key, value in devices.items():
        #print(f"{key:<7s}:{value}")
        # or
        print(f"{key:>16s}:{value}")

    device.append(devices)
print()
print("Devices as a list of dict()")
pprint(device)
print()
print("Tabulated format")

print(tabulate(sorted(device, key=itemgetter('vendor', 'os', 'version')), headers='keys'))

