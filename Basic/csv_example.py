from project.files_formats.inventory import csv_inventory
import csv
from pprint import pprint
from tabulate import tabulate
import filecmp

# Writing and reading csv file same as JSON, YAML and XML
with open("csv_example_inventory.csv", 'w') as csv_out:
    csv_writer = csv.writer(csv_out)
    csv_writer.writerows(csv_inventory)

# Reading the csv file
with open("csv_example_inventory.csv", 'r') as csv_in:
    csv_read = csv.reader(csv_in)
    saved_list = list()
    for device in csv_read:
        saved_list.append(device)

print("\ncsv inventory consists of",saved_list)

print("Printing in better way")
pprint(saved_list)

# Comparing the files
print()
print("Comparing the file written by us and the csv inventory")
if saved_list == csv_inventory:
    print("----->>>The files are the same<<<------")
else:
    print("There has been a mismatch in the file")

# Converting LIST of LIST to DICTIONARY

devices = list()
for device_index in range(1, len(csv_inventory)):
    device = dict()
    for index, header in enumerate(csv_inventory[0]):
        device[header] = csv_inventory[device_index][index]
    devices.append(device)

# printing the dictionary
pprint(devices)

# Reading a csv file and tabulating
with open("spreadsheet_inventory.csv", 'r') as csv_in:
    csv_read = csv.reader(csv_in)
    spreadsheet_inventory = list()
    for device in csv_read:
        spreadsheet_inventory.append(device)

devices = list()
for device_index in range(1, len(spreadsheet_inventory)):
    device = dict()
    for index, header in enumerate(spreadsheet_inventory[0]):
        device[header] = spreadsheet_inventory[device_index][index]
    devices.append(device)

print("\nTabulate output of spreadsheet inventory")
print("\n", tabulate(devices, headers='keys'))

# CONVERT PYTHON DATA BACK TO CSV
headers = devices[0].keys()
with open("python_to_csv.csv", 'w') as csv_out:
    csv_writer = csv.DictWriter(csv_out, headers)
    csv_writer.writeheader()
    csv_writer.writerows(devices)

if filecmp.cmp("spreadsheet_inventory.csv", "python_to_csv.csv"):
    print("\nThe files are same")
else:
    print("\nThe files are not same but expected since the Dictwriter adds an additional line")


