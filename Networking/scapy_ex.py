from sys import flags

import scapy.all as scapy
from scapy.interfaces import ifaces
from scapy.layers.l2 import Ether, ARP
from scapy.layers.inet import IP, ICMP, TCP

## CAPTURING EVERYTHING AND PRINT PACKET SUMMARY
print("\n----- Packet sssssssssssssummariess ---------")
capture = scapy.sniff(iface='ens33', count=10)
print(capture.summary())


## CAPTURE DNS AND PRINT PACKETS
print("\n ----- DNS Packet SUmmary -----------------")
capture = scapy.sniff(iface='ens33', filter="udp port 53", count=10)
print(capture.summary())


# CAPTURE DNS AND PRINT COMPLETE PACKETS
print("\n\n ----- DNS Packets, complete")
capture = scapy.sniff(iface="ens33", filter="udp port 53", count=10)
for packet in capture:
    print(packet.show())


# CAPTURE AND HANDLE PACKETS AS THEY ARRIVE
def print_packet(pkt):
    print("   ",pkt.summary())

scapy.sniff(iface="ens33", prn=print_packet, filter="tcp port https", count=10)

# USING LAMBDA FUNCTION
print("\n ------- Capturring and printing using lambda function --------")
scapy.sniff(iface="ens33", prn=lambda pkt: print(f"lambda    {pkt.summary()}"), filter="tcp port https", count=10)


# Discoveing HOSTS USING MANUAL ARP PING
print("\n -------- Discovoring hosts on network using manual ARP Ping--------------")
ans, uans = scapy.srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.254.0/24"), timeout=2)
ans.summary()


# Discoveing HOSTS USING MANUAL ARP PING FUNCTION
print("\n -------- Discovoring hosts on network using arping() function--------------")
ans, uans = scapy.arping("192.168.254.0/24")
ans.summary()

for res in ans.res:
    print(f"---> IP address discovered: {res[0].payload.pdst}")


# DISCOVER HOSTS ON NETWORKING USING ICMP PING
# print("\n\n----- Discovery hosts on network using ICMP ping ---------------------")
# ans, unans = scapy.sr(IP(dst="192.168.254.1-254")/ICMP())
# ans.summary()

#tcp port scan
while True:
    ip = input("ENter the IP address you want to find port")
    if not ip:
        print("\n Ending Port Scanning")


    answers, unans = scapy.sr(IP(dst=ip)/TCP(flags="S", sport=666, dport=(1,2024)), timeout=10)
    for answered in answers:
        print("\n ----> Open ports: ",answered[0].summary())

    # For unans ips
    for unansd in unans:
        print("\n ----> Closed ports: ", unansd[0].summary())

    print("\n----- Open/Closed port totals --------")
    print(f"\tOpen ports: {len(answers)}")
    print(f"\tClosed ports: {len(unans)}")




