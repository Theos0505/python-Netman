from netmiko import Netmiko


# Below is for napalm connection
cisco_sandbox_type = {
        "ios": {
            #"hostname": "ios-xe-mgmt.cisco.com",  # Alternate ios box
            "hostname": "sandbox-iosxr-1.cisco.com", # Alternate ios box
            "port": 22,
            #'ip': "131.226.217.181",  # IP of alternate box
            'ip': "131.226.217.150", # IP of alternate box
            "username": "admin",
            "password": "C1sco12345",
            "device_type": "cisco_ios"
        },
        "nxos": {
             "hostname": "sbx-nxos-mgmt.cisco.com",
             "port": 22,
             "username": "admin",
             "password": "Admin_1234!",
             "device_type": "cisco_nxos"

        }
    }

def connect(device_type):
    #cisco_sandbox_type = {
    #     "csr": {
    #         #"hostname": "ios-xe-mgmt.cisco.com",  # Alternate ios box
    #         "hostname": "sandbox-iosxr-1.cisco.com", # Alternate ios box
    #         "port": 22,
    #         #'ip': "131.226.217.181",  # IP of alternate box
    #         'ip': "131.226.217.150", # IP of alternate box
    #         "username": "admin",
    #         "password": "C1sco12345",
    #         "device_type": "cisco_ios"
    #     },
    #     "nxos": {
    #          "hostname": "sbx-nxos-mgmt.cisco.com",
    #          "port": 22,
    #          "username": "admin",
    #          "password": "Admin_1234!",
    #          "device_type": "cisco_nxos"
    #
    #     }
    # }

    print(f"\nConnecting to {cisco_sandbox_type[device_type]['hostname']}:{cisco_sandbox_type[device_type]['port']}")
    print("\n\n...,,This might take a while")

    connection = Netmiko(
        cisco_sandbox_type[device_type]['hostname'],
        #ip=cisco_sandbox_type[device_type]['ip'],
        port=cisco_sandbox_type[device_type]['port'],
        username=cisco_sandbox_type[device_type]['username'],
        password=cisco_sandbox_type[device_type]['password'],
        device_type=cisco_sandbox_type[device_type]['device_type']
    )
    return connection


def disconnect(connection):
    connection.disconnect()

