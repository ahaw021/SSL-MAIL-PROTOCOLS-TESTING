import nmap
from constants import *

def scan_mail_server_ports():
    print("Nmap Scanner with Ports and No Service Identification \r\n")
    scanner = nmap.PortScanner
    print("Will Scan SMTP Ports: {},{},{}".format(SMTP_STANDARD,SMTP_IMPLICIT_SSL,SMTP_STARTTLS_SSL))
    print("Will Scan POP Ports: {},{}".format(POP_STANDARD,POP_IMPLICIT_SSL))
    print("Will Scan IMAP Ports: {},{}".format(POP_STANDARD,POP_IMPLICIT_SSL))

def scan_mail_server_ports_services():
    print("Nmap Scanner with Ports with Service Identification \r\n")
    scanner = nmap.PortScanner
    print("Will Scan SMTP Ports: {},{},{}".format(SMTP_STANDARD,SMTP_IMPLICIT_SSL,SMTP_STARTTLS_SSL))
    print("Will Scan POP Ports: {},{}".format(POP_STANDARD,POP_IMPLICIT_SSL))
    print("Will Scan IMAP Ports: {},{}".format(POP_STANDARD,POP_IMPLICIT_SSL))
