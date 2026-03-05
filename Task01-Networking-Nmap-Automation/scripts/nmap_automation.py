import nmap
from datetime import datetime

target = input("Enter target IP: ")

scanner = nmap.PortScanner()
scanner.scan(target, arguments='-sS -sV')

with open("scan_report.txt", "w") as report:
    report.write("Automated Nmap Scan Report\n")
    report.write("Timestamp: " + str(datetime.now()) + "\n")
    report.write("Target: " + target + "\n\n")

    for host in scanner.all_hosts():
        report.write("Host: " + host + "\n")
        report.write("Open Ports:\n")

        for proto in scanner[host].all_protocols():
            ports = scanner[host][proto].keys()
            for port in ports:
                service = scanner[host][proto][port]['name']
                version = scanner[host][proto][port].get('version', '')
                report.write(f"Port: {port} | Service: {service} | Version: {version}\n")

    report.write("\nScan Completed Successfully.\n")

print("Scan finished. Report saved as scan_report.txt")
