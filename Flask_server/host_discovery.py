import scapy.all as scapy
from tabulate import tabulate
import socket
from datetime import datetime
import requests
from operator import itemgetter

hosts = dict()


def discovery():
    # DISCOVER HOSTS ON NETWORK USING ARPING FUNCTION
    print(
        "\n\n----- Discovery hosts on network using arping() function ---------------------"
    )
    ans, uans = scapy.arping("192.168.254.0/24")
    ans.summary()

    for res in ans.res:
        print(f">>>>> IP Address discovered: {res[0].payload.pdst}")

        ip_address = res.payload.psrc
        mac_address = res.payload.hwsrc

        try:
            hostname = socket.gethostbyaddr(str(ip_address))
        except (socket.error, socket.gaierror):
            hostname = (str(ip_address), [], [str(ip_address)])
        last_heard = str(datetime.now())[:-3]

        host = {
            "ip": ip_address,
            "mac": mac_address,
            "hostname": hostname[0],
            "last_heard": last_heard,
            "availability": True,
        }
        # Dict and List point to the same data ; list is for easy tabulation
        hosts[host['hostname']] = host

        print("\n----- Hosts discovered (tabulate) --------------------")
        print("\n", tabulate(sorted(hosts.values(), key=itemgetter("hostname")), headers="keys"))

    rsp = requests.get("http://127.0.0.1:5000/hosts", json=hosts)
    if rsp.status_code != 204:
        print(
            f"{str(datetime.now())[:-3]}: Error posting to /hosts, response: {rsp.status_code}, {rsp.content}"
        )

    response = requests.get("http://127.0.0.1:5000/hosts")
    if response.status_code != 200:
        print(f"get hosts failed: {response.reason}")
        exit()

    hosts_received = response.json()
    # print("\n----- Hosts received from flask mini-quokka --------------------")
    # pprint(hosts_received)

    print("\n----- Compare hosts discovered with hosts retrieved from flask")
    if hosts == hosts_received:
        print("\n     success! hosts discovered equals hosts retrieved")
    else:
        print("\n     oops! hosts retrieved are not equal to what was discovered")

    print("\n----- Hosts received (tabulate) --------------------")
    print("\n", tabulate(sorted(hosts_received.values(), key=itemgetter("hostname")), headers="keys"))