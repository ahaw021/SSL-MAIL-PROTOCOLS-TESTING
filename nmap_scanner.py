import nmap
from constants import *
from connections import *

SCAN_PORTS = "{},{},{},{},{},{},{}".format(SMTP_STANDARD,SMTP_STARTTLS_SSL,SMTP_IMPLICIT_SSL,IMAP_STANDARD,IMAP_IMPLICIT_SSL,POP_STANDARD,POP_IMPLICIT_SSL)
SCANNER = nmap.PortScanner()

def scan_mail_server_standard_ports(hostnames):
    for hostname in hostnames:
        print("\r\nScanning Host: {}. Nmap Scanner - ports only \r\n".format(hostname))
        print("Scanning the following Ports: {} \r\n".format(SCAN_PORTS))
        SCANNER.scan(hostname,SCAN_PORTS,"-Pn")
        for ip in SCANNER.all_hosts():
            for port in SCANNER[ip]['tcp'].keys():
                print("Port {} is {}. Connection Test passed/failed: {} ".format(port,SCANNER[ip]['tcp'][port]['state'],SCANNER[ip]['tcp'][port]['reason']))

def scan_mail_server_standard_ports_services(hostnames):
    for hostname in hostnames:
        print("Scanning Host: {}. Nmap Scanner with Service Identification \r\n".format(hostname))
        print("Scanning the following Ports: {} \r\n".format(SCAN_PORTS))
        SCANNER.scan(hostname,SCAN_PORTS,"-sV -Pn")
        for ip in SCANNER.all_hosts():
            for port in SCANNER[ip]['tcp'].keys():
                print("Port {} is {} and is running the following mail server: {}. Connection Test passed/failed: {}  ".format(port,SCANNER[ip]['tcp'][port]['state'],SCANNER[ip]['tcp'][port]['product'],SCANNER[ip]['tcp'][port]['reason']))
