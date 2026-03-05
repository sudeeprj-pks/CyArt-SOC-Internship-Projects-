# Task 01 – Networking Fundamentals, Nmap Scanning and Automation

##  Overview

This project demonstrates the fundamentals of networking, Nmap scanning techniques, and automation using Python.  
The objective of this task was to understand how devices communicate in a network, identify open ports and services using Nmap, analyze security risks, and automate scanning using a Python script.

The lab environment was created using **Kali Linux** as the attacker machine and **Metasploitable** as the vulnerable target machine.

---

##  Lab Environment

| Machine | Role | IP Address |
|-------|------|-----------|
| Kali Linux | Attacker | 192.168.100.10 |
| Metasploitable | Target | 192.168.100.20 |

Network Type: **VirtualBox Internal Network**

---

##  Tools Used

- Kali Linux
- Nmap
- Python
- VirtualBox
- Metasploitable
- draw.io (Network Diagram)

---

##  Networking Fundamentals

### IP Address
An IP address uniquely identifies a device on a network. It allows systems to communicate with each other.

Example used in this lab:

- Kali Linux → `192.168.100.10`
- Metasploitable → `192.168.100.20`

---

### Ports

Ports allow multiple services to run on a single IP address.

Common ports discovered:

| Port | Service |
|-----|--------|
| 21 | FTP |
| 22 | SSH |
| 23 | Telnet |
| 80 | HTTP |
| 3306 | MySQL |

---

### TCP vs UDP

**TCP (Transmission Control Protocol)**

- Reliable
- Connection oriented
- Uses 3-way handshake

**UDP (User Datagram Protocol)**

- Faster
- Connectionless
- Less reliable

---

#  Nmap Scanning

### SYN Scan
nmap -sS 192.168.100.20 -oN syn_scan.txt


This scan performs a half-open connection and is considered stealthier than other scans.

---

### TCP Connect Scan

nmap -sT 192.168.100.20 -oN tcp_scan.txt


This scan completes the full TCP three-way handshake.

---

### UDP Scan
nmap -sU 192.168.100.20 -oN udp_scan.txt

Used to identify services running on UDP ports.

---

### OS Detection

nmap -O 192.168.100.20

Attempts to detect the operating system of the target.

---

# 📊 Scan Results

The following services were identified:

| Port | Service | Description |
|-----|--------|-------------|
| 21 | FTP | File transfer service |
| 22 | SSH | Secure remote login |
| 23 | Telnet | Remote login service |
| 80 | HTTP | Web server |
| 3306 | MySQL | Database service |

---

# ⚠ Risk Analysis

Some discovered services may pose security risks:

**FTP – Port 21**

- Version: vsftpd 2.3.4
- Known vulnerability: CVE-2011-2523 (Backdoor)

**Telnet – Port 23**

- Transmits credentials in plain text
- Vulnerable to interception

**MySQL – Port 3306**

- Potential database exposure risk

---

# 🤖 Python Automation

A Python script was developed using the **python-nmap** library.

Features of the script:

- Accepts target IP
- Runs automated Nmap scan
- Extracts open ports
- Generates scan report

Run the script:
python3 nmap_automation.py


Output file generated:
scan_report.txt


---

#  Network Diagram

The network diagram shows the attacker machine (Kali Linux) scanning the target machine (Metasploitable) inside an isolated internal network.

---

#  Project Structure

Task01-Networking-Nmap-Automation
│
├── report
│ └── TASK01 SUB.pdf
│
├── screenshots
│
├── scripts
│ └── nmap_automation.py
│
├── scan-results
│
└── network-diagram

---

#  Key Learnings

- Understanding IP addressing and ports
- Performing multiple Nmap scanning techniques
- Analyzing scan outputs
- Identifying potential vulnerabilities
- Automating security tasks using Python

---

#  Author

**Sudeep RJ  
Cyber Security Intern – CyArt
