from netmiko import Netmiko


def connect(device_type):
    cisco_sandbox_type = {
        "csr": {
            "hostname": "ios-xe-mgmt.cisco.com",
            "port": 8181,
            'ip': "131.226.217.149",
            "username": "developer",
            "password": "C1sco12345",
            "device_type": "cisco_ios"
        },
        "nxos": {
             "hostname": "sbx-nso-mgmt.cisco.com",
             "port": 8181,
             "username": "admin",
             "password": "Admin_1234!",
             "device_type": "cisco_nxos"

        }
    }

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

