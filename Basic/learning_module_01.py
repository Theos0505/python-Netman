
# This file is f an example purpose which prints the multiple devices created and returned by utils.py

from utility.utils import creat_devices  # Local module is being called which returns multiple devices
from tabulate import tabulate  # Tabulate the given list

if __name__ == '__main__':
    devices = creat_devices(3, 1)  # passing by parameter
    print("\n", tabulate(devices, headers="keys"))
