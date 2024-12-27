from inventory import inventory
import yaml

# Convert inventory to YAML and write to file
with open("inventory.yaml", "w") as yaml_out:
    yaml_out.write(yaml.dump(inventory, indent=4))  # This creates a .json file with the inventory data

# Read the YAML data file
with open("inventory.yaml", "r") as yaml_read:
    yaml_inventory = yaml_read.read()

# Printing the inventory
print("inventory.yaml file: \n", yaml_inventory)

# Converting YAML inventory to python and then convert it back to YAML
print(yaml.dump(yaml.safe_load(yaml_inventory), indent=4))

# Checking if saved inventory is same as inventory file
saved_inventory = yaml.safe_load(yaml_inventory)

if saved_inventory == inventory:
    print("------Saved inventory is same as inventory file----------")
else:
    print("--------The file is not same as each other--------")

# Reading the formatted yaml file with curly brackets
print("\n\n Reading formatted yaml file name formatted_inventory.yaml: ")
with open("formatted_inventory.yaml", 'r') as yaml_in:
    yaml_formatted_inventory = yaml_in.read()

print(yaml_formatted_inventory)
# Checking if saved formatted inventory is same as inventory file
saved_formatted_inventory = yaml.safe_load(yaml_formatted_inventory)

if saved_formatted_inventory == inventory:
    print("------Saved formatted inventory is same as inventory file----------")
else:
    print("--------The file is not same as each other--------")

# Printing the yaml data as same as python dictionaries
print(yaml.dump(yaml.safe_load(yaml_inventory), indent=4, default_flow_style=True))
