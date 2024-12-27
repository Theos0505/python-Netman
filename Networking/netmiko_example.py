from netmiko_connect import connect
import re

show_arp = "arp"
show_int_brief = "int brief"
show_int_description = "int description"
show_ip_route = "ip route"
show_version = "version"

csr = 'csr'
nxos = 'nxos'

commands = {
    show_ip_route: {csr: "show ip route",
                    nxos: "show ip route"},
    show_arp: {csr: "show arp",
               nxos: "show arp"},
    show_int_description: {csr: "show int description",
                           nxos: "show int description"},
    show_int_brief: {csr: "show int brief",
                     nxos: "show int brief"},
    show_version: {csr: "show version",
                   nxos: "show version"}
}

for device_type in [csr, nxos]:
    connection = connect(device_type)
    print("connection: ", connection)

    print(f"\n\nShowing running config for {device_type} ------------")
    output = connection.send_command("show running config")
    print(output)

    print(f"\n\nShowing ip route of {device_type} ------------")
    output = connection.send_command(commands[show_ip_route][device_type])
    print(output)

    print(f"\n\nShowing arp entry of {device_type} ------------")
    output = connection.send_command(commands[show_arp][device_type])
    print(output)

    print(f"\n\nShowing interface brief of {device_type} ------------")
    output = connection.send_command(commands[show_int_brief][device_type])
    print(output)

    print(f"\n\nShowing interface description of {device_type} ------------")
    output = connection.send_command(commands[show_int_description][device_type])
    print(output)

    print(f"\n\nShowing version of {device_type} ------------")
    output = connection.send_command(commands[show_version][device_type])
    print(output)

    connection.disconnect()

print("\n\nCycling through the commands")
csr_connection = connect(csr)
nxos_connection = connect(nxos)

csr_version_raw = None
nxos_version_raw = None
if csr_connection and nxos_connection:
    print("\nconnection successfull...")
else:
    exit()

for command_type, command in commands.items():
    print("\n Showing output for {}".format(command_type))

    print("\n....for CSR: {}------".format(command[csr]))
    csr_output = csr_connection.send_command(command[csr])
    print(output)

    print("\n....for NXOS: {}------".format(command[nxos]))
    nxos_output = nxos_connection.send_command(command[nxos])
    print(output)

    if command_type == show_version:
        csr_version_raw = csr_output
        nxos_version_raw = nxos_output

csr_connection.disconnect()
nxos_connection.disconnect()




