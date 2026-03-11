import pyshark
import matplotlib.pyplot as plt
from collections import Counter

capture = pyshark.FileCapture('https_traffic_capture.pcapng')

packet_sizes = []
ip_counter = Counter()

for packet in capture:
    try:
        size = int(packet.length)
        packet_sizes.append(size)

        src = packet.ip.src
        dst = packet.ip.dst

        ip_counter[src] += 1
        ip_counter[dst] += 1

    except AttributeError:
        continue

print("Packet Communication Count")
print(ip_counter)

plt.hist(packet_sizes, bins=20)
plt.title("Packet Size Distribution")
plt.xlabel("Packet Size")
plt.ylabel("Frequency")

plt.show()
