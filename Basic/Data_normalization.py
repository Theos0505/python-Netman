from ipaddress import IPv4Address

# --------Starting Data Normaloization


data_1 = {
    "name": "sbx-nn9kv-ao",
    "vendor": "cisco",
    "model": 'Nexus9000 c9300v chassis',
    "os": 'nxos',
    "version": '9.3(3)',
    "ip": '10.1.1.1',
    1: "any data goes here",
}

data_2 = {
    "name": "SBX-nn9kv-ao",
    "vendor": "Cisco",
    "model": 'Nexus9000 c9300v chassis',
    "os": 'NXOS',
    "version": '9.3(3)',
    "ip": '10.1.1.1',
    1: "any data goes here",
}

if (
        data_1['name'].lower() == data_2['name'].lower() and
        data_1['vendor'].lower() == data_2['vendor'].lower() and
        data_1['model'].lower() == data_2['model'].lower() and
        data_1['os'].lower() == data_2['os'].lower()
):
    print("--> String lower() normalization works")
else:
    print("--> String lower() normalization does not work")

if (
        data_1['name'].casefold() == data_2['name'].casefold() and
        data_1['vendor'].casefold() == data_2['vendor'].casefold() and
        data_1['model'].casefold() == data_2['model'].casefold() and
        data_1['os'].casefold() == data_2['os'].casefold()
):
    print("--> String casefold() normalization works")
else:
    print("--> String casefold() normalization does not work")

# ------MAC address normalization-----

mac_addr_colons = 'a0:b1:c2:d3:e4:f5'
mac_addr_caps = 'A0:B1:C2:D3:E4:F5'
mac_addr_dots = 'a0b1.c2d3.e4f5'
mac_addr_hyphens = 'A0-B1-C2-D3-E4-F5'
mac_addr_wacky = 'A0-B1:c2d3:e4-F5'

mac_addr_norm = 'a0b1c2d3e4f5'


def data_norm(mac):
    return mac.lower().replace(':', "").replace("-", "").replace(".", "")


if (
        data_norm(mac_addr_colons)
        == data_norm(mac_addr_caps)
        == data_norm(mac_addr_dots)
        == data_norm(mac_addr_dots)
        == data_norm(mac_addr_wacky)
        == mac_addr_norm
):
    print("--> mac normalization works")
else:
    print("-->mac normalization doesn't work")

# IPv4 Normalization

ippaddr_1 = '10.0.1.1'
ippaddr_2 = '10.00.001.001'
ippaddr_3 = '010.0.01.001'

if IPv4Address(ippaddr_1) == IPv4Address(ippaddr_2) == IPv4Address(ippaddr_3):
    print("--> IP address normalization works")
else:
    print("--> Ip address normalization does not work")
