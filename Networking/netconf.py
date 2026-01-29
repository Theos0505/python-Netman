from ncclient import manager
from lxml import etree
import xmltodict
from pprint import pprint



# the following comment/lines are to workaround a PyCharm bug
# noinspection PyUnresolvedReferences

from xml.dom.minidom import parseString



csr_device = {
    "host": "ios-xe-mgmt.cisco.com",
    "port": 10000,
    "username": "developer",
    "password": "C1sco12345",
    "device_params": {"name": "csr"},
}

iosxr_device = {
        "host": "sandbox-iosxr-1.cisco.com",
        "port": 830,
        "username": "admin",
        "password": "C1sco12345",
        "device_params": {"name": "iosxr"},

}

nxos_device = {
    "host": "sandbox-nxos-1.cisco.com",
    "port": 830,
    "username": "admin",
    "password": "Admin_1234!",
    "device_params": {"name": "nexus"},
}

for device in [nxos_device, iosxr_device]:

    print(f"\n-------- Connecting to device {device['host']} ----------")

    nc_connection = manager.connect(
        host=device["host"],
        port=device["port"],
        username=device["username"],
        password=device["password"],
        device_params=device["device_params"]
    )

    print("\n --------- Connected -------------")

    if device["device_params"]["name"] == "nexus":
        # GETTING SPECIFIC PART OF XML SUBTREE WITH GET()
        serial_number_xml_nxos = '<System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device"><serial/></System>'

        spc = nc_connection.get(("subtree", serial_number_xml_nxos))
        print(f"\n------- XML subtree from host {device["host"]}")
        print(str(etree.tostring(spc.data_ele, pretty_print=True).decode()))

    else:
        # GETTING THE WHOLE CONFIG AND PARSING

        config = nc_connection.get_config("running")
        print(f"\n------- XML get_config() from host {device["host"]}")
        print(str(etree.tostring(config.data_ele, pretty_print=True).decode()))

        xml_data = parseString(str(config))
        version = xml_data.getElementsByTagName("version")
        print(f"\n----- Device OS version, hostname, email from: {device['host']}")

        if len(version) > 0:
            print(f"     version:{version[0].firstChild.nodeValue}")
        else:
            print(f"     Unable to fetch version")

        hostname = xml_data.getElementsByTagName("hostname")
        if len(hostname) > 0:
            print(f"     version:{hostname[0].firstChild.nodeValue}")
        else:
            print(f"     Unable to fetch hostname")

        email = xml_data.getElementsByTagName("email")
        if len(email) > 0:
            print(f"     version:{email[0].firstChild.nodeValue}")
        else:
            print(f"     Unable to fetch email")

        usernames = xml_data.getElementsByTagName("username")
        for username in usernames:
            name = xml_data.getElementsByTagName("name")
            if len(name) > 0:
                print(f"     version:{name[0].firstChild.nodeValue}")
            else:
                print(f"     Unable to fetch username")

        version_filter = """
        
                        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                        <version></version>
                        </native>
                        
                        """
        spc = nc_connection.get(("subtree", version_filter))
        print(f"\n------- XML subtree from host {device["host"]}")
        print(str(etree.tostring(spc.data_ele, pretty_print=True).decode()))

        cpu_filter = """
                    <filter>
                    <cpu-usage xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-process-cpu-oper">
                    </cpu-usage>
                    </filter>
                    
                    """

        spc = nc_connection.get(("subtree", cpu_filter))
        print(f"\n------- XML subtree from host {device["host"]}")
        print(str(etree.tostring(spc.data_ele, pretty_print=True).decode()))

        memory_filter = """
                            <filter>
                            <memory-statistics xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-memory-oper">
                            </memory-statistics>
                            </filter>

                            """

        spc = nc_connection.get(("subtree", memory_filter))
        print(f"\n------- XML subtree from host {device["host"]}")
        print(str(etree.tostring(spc.data_ele, pretty_print=True).decode()))
        
        memory_statistics = xmltodict.parse(

                    str(etree.tostring(rsp.data_ele, pretty_print=True).decode()),
                    dict_constructor=dict,
        )

        print("\n----- Memory statistics --------------------\n")
        pprint(memory_statistics)
        config_python = xmltodict.parse(
                        str(etree.tostring(config.data_ele, pretty_print=True).decode()),
                        dict_constructor=dict,

        )

        pprint(config_python)
















