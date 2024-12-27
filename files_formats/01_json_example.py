from inventory import inventory
import json

# Convert inventory to json and write to file
with open("inventory.json", "w") as json_out:
    json_out.write(json.dumps(inventory, indent=4))  # This creates a .json file with the inventory data

# Read the json data file
with open("inventory.json", "r") as  json_read:
    json_inventory = json_read.read()

# Printing the inventory
print("inventory.json file: ", json_inventory)

# Converting Json inventory to python and then convert it back to string
print(json.dumps(json.loads(json_inventory), indent=4))

# Checking if saved inventory is same as inventory file
saved_inventory = json.loads(json_inventory)

if saved_inventory == inventory:
    print("------Saved inventory is same as inventory file----------")
else:
    print("--------The file is not same as each other--------")