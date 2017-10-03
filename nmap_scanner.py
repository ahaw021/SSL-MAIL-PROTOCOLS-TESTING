import nmap
from constants import *

SCAN_PORTS = "{},{},{},{},{},{},{}".format(SMTP_STANDARD,SMTP_STARTTLS_SSL,SMTP_IMPLICIT_SSL,IMAP_STANDARD,IMAP_IMPLICIT_SSL,POP_STANDARD,POP_IMPLICIT_SSL)
SCANNER = nmap.PortScanner()

def scan_mail_server_ports(hostname):
    print("Scanning Host: {}. Nmap Scanner with No Service Identification \r\n".format(hostname))
    print("Scanning the following Ports: {} \r\n".format(SCAN_PORTS))
    results_dict = SCANNER.scan(hostname,SCAN_PORTS,"-Pn")
    print(results_dict)

def scan_mail_server_ports_services(hostname):
    print("Scanning Host: {}. Nmap Scanner Service Identification \r\n".format(hostname))
    print("Scanning the following Ports: {} \r\n".format(SCAN_PORTS))
    results_dict = SCANNER.scan(hostname,SCAN_PORTS)
    print(results_dict)
