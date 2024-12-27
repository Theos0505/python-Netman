
# This program is for an example on how to import the local .py file as a module
# Here both the variable and the function is imported to "learning module.py" script


inventory = [
    {
        "name" : "Cisco switch 2040",
        "ssh-info": {
            "hostname": "ios-xe-mgmt-latest.cisco.com",
            "port": 8181,
            "credentials": {"username": "developer", "password": "Cisco12345"},
            "device type": "cisco_ios",
        },
        "netconf-info": {
            "port" : 10000
        },
        "restconf-info": {"port":9443}
    },
    {
        "name" : "Cisco switch 2040",
        "ssh-info": {
            "hostname": "ios-xe-mgmt-latest.cisco.com",
            "port": 8181,
            "credentials": {"username": "developer", "password": "Cisco12345"},
            "device type": "cisco_ios",
        }
    },
]

def _get_inventory():
    return inventory