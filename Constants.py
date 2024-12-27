from random import choice, randrange
from pprint import pprint
import string


class Vendor:
    CISCO = 'cisco'
    ARISTA = 'arista'
    JUNIPER = 'juniper'

# Using ENUM to avoid string literals
class Vendor_1(Enum):
    CISCO = 1
    ARISTA = 2
    JUNIPER = 3

devices = dict()
created_devices = list()


for i in range(20):

    # Using Class variables to assign values
    # devices['name'] = (choice(['r2', 'r3', 'r4', 'r5', 'r6']) + choice(['L', 'U']) + choice(string.ascii_letters))
    # devices['vendor'] = choice([Vendor.CISCO, Vendor.ARISTA, Vendor.JUNIPER])
    #
    # if devices['vendor'] == "cisco":
    #     devices['os'] = choice(["ios", "iosxe", "iosxr", "nexus"])
    #     devices['version'] = choice(["12.1.(T).04", "14.07x", "8.12(S).810", "20.45"])
    # elif devices['vendor'] == "jupitor":
    #     devices['os'] = choice("junos")
    #     devices['version'] = choice(["J6.23.1", "8.43.12", "6.45", "6.03"])
    # elif devices['vendor'] == "arista":
    #     devices['os'] = choice("eos")
    #     devices['version'] = choice(["2.45", "2.55", "2.92.145", "3.01"])
    # created_devices.append(devices)


pprint(created_devices)