import pyshark

def packet_summary(pkt):
    print("     ", str(pkt)[:120])

# CAPTURE EVERYTHING AND PRINT PACKET SUMMARIES
print("\n ----- Packet summary -------")
capture_all = pyshark.LiveCapture(interface="ens33", only_summaries=True)
capture_all.sniff(packet_count=10)
for packet in capture_all:
    packet_summary(packet)

# CAPTURE DNS TRAFFIC AND PRINT PACKET SUMMARIES
print("\n ----- DNS Packet summary -------")
capture_dns = pyshark.LiveCapture(interface="ens33", only_summaries=True, bpf_filter="udp port 53")
capture_dns.sniff(packet_count=10)
for packet in capture_dns:
    packet_summary(packet)


# CAPTURING AND PRINTING COMPLETE PACKETS
print("\n ----- Printing Complete Packet -------")
capture_full = pyshark.LiveCapture(interface="ens33")
capture_full.sniff(packet_count=10)
for packet in capture_full:
    print(packet)

# CAPTURING AND ANALYSING HTTPS PACKETS
print("\n ----- Https Packet summary -------")
capture_web = pyshark.LiveCapture(interface="ens33", only_summaries=True, bpf_filter="tcp port https")
capture_web.apply_on_packets(packet_summary,packet_count=10)


# CAPTURING AND ANALYSING HTTPS PACKETS USING LAMBDA FUNCTIONS
print("\n ----- Https Packet summary -------")
capture_http = pyshark.LiveCapture(interface="ens33", only_summaries=True, bpf_filter="tcp port https")
capture_http.apply_on_packets(lambda pkt: print("lambda    ", str(pkt)[:114]),packet_count=10)


# CAPTURING AND ANALYSING HTTPS PACKETS AND PRINTING THEM WITH SNIFF CONTINUOUSLY
print("\n ----- Printing packets as they arrive with sniff_continuously() -------")
capture_http2 = pyshark.LiveCapture(interface="ens33", only_summaries=True, bpf_filter="tcp port https")
for packet in capture_http2.sniff_continuously(packet_count=10):
    packet_summary(packet)



# TAKING BPF FILTER INPUT
print("\n ------ USER INPUT FOR BPF FILTER ----------")
while True:

    bpf_filter = input("\nEnter bpf filter")
    if not bpf_filter:
        break

    print(f"\n ----- Capturing packets with bpf filter: {bpf_filter} -------")
    capture_bpf = pyshark.LiveCapture(interface="ens33", only_summaries=True, bpf_filter=bpf_filter)

    try:
        capture_web.apply_on_packets(packet_summary, packet_count=10)
    except KeyboardInterrupt as e:
        continue



