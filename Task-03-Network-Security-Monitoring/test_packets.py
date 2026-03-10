
from scapy.all import IP, TCP, send
import time

target_ip = "10.0.2.15"

ports = range(1, 50)

print("Starting SYN scan simulation...")

for port in ports:
    packet = IP(dst=target_ip)/TCP(dport=port, flags="S")
    send(packet, verbose=False)
    print(f"Sent SYN packet to port {port}")
    time.sleep(0.2)

print("Simulation finished.")
