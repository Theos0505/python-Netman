from project.utility.utils import creat_devices  # Local module to create devices
from pprint import pprint  #pretty print module
from operator import itemgetter
from tabulate import tabulate
from random import choice
from datetime import datetime
from time import sleep


devices = creat_devices(25)  # Creating devices
'''print("******Using Normal print******")
print(devices)'''

print()

print("******Using pprint******")
pprint(devices)

print()

'''print("******Using Loop******")
for device in devices:
    sleep(0.1)  # delay in printing
    device["last heard"] = str(datetime.now())  # adds an entry 'last heard'
    print(device)'''

print()

'''print("******Using tabulate******")
print(tabulate(sorted(devices, key=itemgetter('vendor', 'os', 'version')), headers="keys"))'''

print()

'''print("*******Using sorting wrt last heard******")
print("    NAME        VENDOR :OS       IP ADDRESS      LAST HEARD")
print("   ------      -------- ------  ------------    -----------")
for device in sorted(devices, key=itemgetter("last heard"),reverse=True):

    print(f'{device["name"]:>8}  {device["vendor"]:>11}: {device["os"]:<7}  {device["ip"]:<14}  {device["last heard"]}')'''

print()

'''print("printing MULTIPLE PRINT STATEMENTS IN SAME LINE")
for device in devices:
    print(f"---testing devices {device['name']}---",end=" ")
    sleep(choice([0.1, 0.2, 0.3]))
    print("....done")
print(" Testing Complete ")'''

print()

import nmap

nm = nmap.PortScanner()
nm.scan('127.0.0.1', '22-443')


