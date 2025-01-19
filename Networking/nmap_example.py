from nmap import PortScanner, PortScannerAsync

from pprint import pprint



nm = PortScanner()



while True:


    ip = input("\nInput IP address to scan: ")

    if not ip:
        break

    print(f"\n--- beginning scan of {ip}")

    output = nm.scan(ip, '22-1024', arguments="-sS -sU -O --host-time 600")

    print(f"--- --- command: {nm.command_line()}")


    print("----- nmap scan output -------------------")

    pprint(output)


    # DEMYSTIFYING TREATING CLASS LIKE DICT

    scan_output_1 = nm[ip]  # 'nm' is a class - why can you do this? __getitem__ in PortScanner

    scan_output_2 = nm._scan_result['scan'][ip]  # this is what __getitem__ returns
    print(f"\n Scan output reference comparison: {scan_output_2 == scan_output_1}\n")

    try:

        print(nm[ip].all_tcp())
        print(nm[ip].all_udp())
        print(nm[ip].all_ip())

    except KeyError as e:
        print(f"\n Failed to get scan result for {ip}")

    print(f"\n End of scan for {ip}")

# # Scanning all hosts in subnet for port 80
# nm.scan("192.168.254.0/24", arguments="-p 80 -open")
# print("\niterating all hosts found in scan for port 22(http)")
# for host in nm.all_hosts():
#     print("---- ----", host)
#
# # Scanning all hosts in subnet for port 22
# nm.scan("192.168.254.0/24", arguments="-p 22 -open")
# print("\niterating all hosts found in scan for port 22(ssh)")
# for host in nm.all_hosts():
#     print("---- ----", host)


# Scanning all hosts in subnet using ICMP
nm.scan("192.168.1.0/29", arguments="-PE")
print("\niterating all hosts found in scan using ICMP ECHO")
for host in nm.all_hosts():
    print("---- ----", host)


def discovered_host(found_host, scan_result):
    if scan_result['nmap']['scanstats']['uphosts'] == '1':
        print(f"--- --- found host: {found_host} scan: {scan_result['nmap']['scanstats']}")


nma = PortScannerAsync()
print("\n Scanning all hosts in network using ICMP ECHO with a callback")
nma.scan("192.168.1.0/29", callback=discovered_host, arguments="-PE")
while nma.still_scanning():
    nma.wait(5)







