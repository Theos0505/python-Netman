"""from inventory import inventory  # importing the 'inventory.py' and importing only the variable

print("This is the dictionary ", inventory)
data = inventory

for i in range(len(data)):
    for key, value in data[i].items():  # Accessing the dictionary items
        print(f" {key}: {value}")  # Printing the value of the particular key
"""

# Another method to import

"""from inventory import _get_inventory as gt  # importing the 'inventory.py' and importing the function as gt which 

print("This is the dictionary ", gt())
data = gt()

for i in range(len(data)):
    for key, value in data[i].items():  # Accessing the dictionary items
        print(f" {key}: {value}")  # Printing the value of the particular key
"""
