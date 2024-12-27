import xmltodict
from inventory import xml_inventory
from pprint import pprint

# Opening python format inventory and writing it in xml format
with open("inventory.xml", 'w') as xml_out:
    xml_out.write(xmltodict.unparse(xml_inventory, pretty=True))

# Loading the xml data and converting it to python format
with open("inventory.xml", 'r') as xml_in:
    saved_inventory = xmltodict.parse(xml_in.read(), )

# Printing the xml inventory in python format
pprint(saved_inventory)

# Printing xml version of the inventory
print("\n")
print(xmltodict.unparse(saved_inventory, pretty=True))

# Checking if the xml format file and python inventory is same
if saved_inventory == xml_inventory:
    print("\nThe inventory is same")
else:
    print("\nThe files are different")
