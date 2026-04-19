import subprocess
from datetime import datetime, timedelta
import nmap
import scapy.all as scapy
import requests
import socket
from time import sleep

MONITOR_INTERVAL = 60
DISCOVERY_INTERVAL = 600
PORTSCAN_INTERVAL = 3600


def get_hosts():
    print("\n\n..... Retrieving hosts ...", end="")
    resp = requests.get("http://127.0.0.1:5000/hosts")
    if resp.status_code != 200:
        print(f" !!!  Failed to retrieve hosts from server: {resp.reason}")
        return {}

    print(" Hosts successfully retrieved")
    return resp.json()


def ping_host(host):
    try:
        print(f"----> Pinging host: {host['hostname']}", end="")
        subprocess.check_output(
            ["ping", "-c3", "n", "i0.5", "-W2", host["ip"]]

        )
        host['availability'] = True
        host['last_heard'] = str(datetime.now())[:-3]
        print(f" Host ping successful: {host['hostname']}")
    except:
        host['availability'] = False
        print(f" !!!  Host ping failed: {host['hostname']}")


def update_host(host):
    print(f".......Updating the Gost info using REST API: {host['hostname']}", end="")

    rsp = requests.put("http://127.0.0.1:5000/hosts", params={"hostname": host['hostname']}, json=host)

    if rsp.status_code != 204:
        print(
            f"{str(datetime.now())[:-3]}: Error posting to /hosts, response: {rsp.status_code}, {rsp.content}"
            )
    else:
        print(f" Successfully updated host status via REST API: {host['hostname']}")


def discovery():
    # DISCOVER HOSTS ON NETWORK USING ARPING FUNCTION
    print(
        "\n\n----- Discovery hosts on network using arping() function ---------------------"
    )
    ans, uans = scapy.arping("192.168.254.0/24")
    ans.summary()

    existing_hosts = get_hosts()

    for res in ans.res:
        print(f">>>>> IP Address discovered: {res[0].payload.pdst}")

        ip_address = res.payload.psrc
        mac_address = res.payload.hwsrc

        try:
            hostname = socket.gethostbyaddr(str(ip_address))
        except (socket.error, socket.gaierror):
            hostname = (str(ip_address), [], [str(ip_address)])
        last_heard = str(datetime.now())[:-3]

        if hostname in existing_hosts:
            continue

        host = {
            "ip": ip_address,
            "mac": mac_address,
            "hostname": hostname[0],
            "last_heard": last_heard,
            "availability": True,
            "open_tcp_ports": []
        }
        update_host(host)


def portscan_hosts(hosts):

    for host in hosts.values():

        if "availability" not in host or not host['availability']:
            continue

        ip = host["ip"]
        print(f"====> Scanning host: {host['hostname']} at IP: {host['ip']}")

        scn = nmap.PortScanner()
        scn.scan(ip, '22-1024')  # arguments="-sS -sU -O --host-time 600" --> optional

        try:
            scn[ip]
        except KeyError as e:
            print(f" !!!  Scan failed: {e}")
            continue

        print(f"===> Scan results: {scn[ip].all_tcp()}")
        host["open_tcp_ports"] = scn[ip].all_tcp()
        update_host(host)


def main():
    last_discovery = datetime.now() - timedelta(days=1)
    last_portscan = datetime.now() - timedelta(days=1)

    while True:
        if (datetime.now() - last_discovery).total_seconds() > DISCOVERY_INTERVAL:
            discovery()
            last_discovery = datetime.now()
        hosts = get_hosts()
        if (datetime.now() - last_portscan).total_seconds() > PORTSCAN_INTERVAL:
            portscan_hosts(hosts)
            last_portscan = datetime.now()

        for host in hosts.values():
            ping_host(host)
            update_host(host)

        sleep(MONITOR_INTERVAL)


if __name__ == "__main__":
    try:
        main()
    except:
        print("\n\nExiting hot-monitor")
        exit()
