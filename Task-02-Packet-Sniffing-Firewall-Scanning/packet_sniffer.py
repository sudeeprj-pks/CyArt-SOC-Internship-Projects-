from scapy.all import sniff, TCP, UDP, ICMP
import matplotlib.pyplot as plt

# Packet counters
tcp_count = 0
udp_count = 0
icmp_count = 0

def packet_callback(packet):
    global tcp_count, udp_count, icmp_count
    
    if packet.haslayer(TCP):
        tcp_count += 1
        print("TCP Packet Captured")
        
    elif packet.haslayer(UDP):
        udp_count += 1
        print("UDP Packet Captured")
        
    elif packet.haslayer(ICMP):
        icmp_count += 1
        print("ICMP Packet Captured")

print("Capturing packets... Press CTRL+C to stop")

try:
    sniff(prn=packet_callback, store=0)
except KeyboardInterrupt:
    print("\nStopping capture...")

protocols = ['TCP', 'UDP', 'ICMP']
counts = [tcp_count, udp_count, icmp_count]

print("Packet Counts:")
print("TCP:", tcp_count)
print("UDP:", udp_count)
print("ICMP:", icmp_count)

plt.bar(protocols, counts)
plt.title("Network Protocol Distribution")
plt.xlabel("Protocol Type")
plt.ylabel("Packet Count")
plt.savefig("protocol_chart.png")

print("Protocol chart saved as protocol_chart.png")
