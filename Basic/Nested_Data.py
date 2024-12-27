import copy

from utility.utils import create_network
from pprint import pprint

network = create_network(4,4)
pprint(network)

print("---> List of all subnets", network['subnet'].keys())
print("Formated printing")
print()
for subnet_address, subnet in network['subnet'].items():
    print(f"---- subnet: {subnet_address}")
    for device in subnet['devices']:
        print(f"|---- {device['name']:8} {device['ip']:10} {device['os']:>10s}:{device['version']:}")


print("\nDiffernce between network assign/shallow copy/deep copy")

network_assign = network  # The network_assign variable points to network variable in the memory
network['subnet']['10.0.1.0']['devices'][0]['name'] = "different assigned name"
print(f"|----network = network_assign: {network_assign == network}")

network_copy = copy.copy(network)
network['subnet']['10.0.1.0']['devices'][0]['name'] = "another name, copy this time"
print(f"|----network = network_copy: {network_copy == network}")

network_deepcopy = copy.deepcopy(network)
network['subnet']['10.0.1.0']['devices'][0]['name'] = "This time deepcopy"
print(f"|----network = network_deepcopy: {network_deepcopy == network}")  # This returns false since it doesn't point to the variable and copys all the data
# so when it compares with that data there is a change tha we did on line 29
