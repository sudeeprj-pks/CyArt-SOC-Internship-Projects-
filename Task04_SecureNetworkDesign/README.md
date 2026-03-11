Task 4 — Secure Network Design, Penetration Testing & Encrypted Traffic Analysis
Objective

Design a secure network architecture and perform penetration testing against a vulnerable machine while analyzing encrypted traffic.

Activities Performed

Secure network topology design

Vulnerability scanning using Nmap

Exploitation testing using Metasploit

Capturing HTTPS traffic using Wireshark

Python-based packet analysis using PyShark

Data visualization using Matplotlib

Example Exploitation Workflow
Kali Linux (Attacker)
       │
       │ Metasploit / Netcat
       ▼
Metasploitable (Target)
       │
       │ HTTPS Traffic Capture
       ▼
Python Traffic Analysis
       │
       ▼
Packet Size Visualization
Python Traffic Analyzer

The Python script traffic_analyzer.py processes the captured PCAP file and generates a packet size distribution chart.

Run the script:

python3 traffic_analyzer.py

Output:

Packet Size Distribution Graph
Learning Outcomes

Through these projects I gained practical experience in:

Network scanning and reconnaissance

Packet capture and traffic analysis

Security monitoring techniques

Exploitation workflows

Python-based traffic analysis

SOC investigation processes

Author

Sudeep R J
Cybersecurity Enthusiast | SOC Analyst Aspirant

GitHub
https://github.com/sudeeprj-pks
