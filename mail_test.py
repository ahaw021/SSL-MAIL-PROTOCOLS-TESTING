import argparse

from testing_providers import *
from openssl_syntax_output import *
from constants import *
from connections import *
from nmap_scanner import scan_mail_server_standard_ports
import json

parser = argparse.ArgumentParser(description="Testing Tool for TLS/SSL Protocols for Mail Servers")

parser.add_argument( '-domains', nargs='*', default="smtp.gmail.com", help="Domains to Scan. Multiple Domains can be provided")
parser.add_argument( '-tlssuites',nargs="*", choices=OPENSSL_TLS_SUITES,default=["tls1_2","tls1_3"], help="TLS Suite as Per OpenSSL Syntax. If not specific TLS 1.2 and TLS 1.3 will be used. ")
parser.add_argument( '-protocols', nargs='*' ,choices=MAIL_PROTOCOLS, default=["smtp", "pop3", "imap"], help="Mail Protocols to Scan. Will Default to all 3.")
parser.add_argument( '-ports', type=int, nargs='*', default=COMMON_MAIL_PORTS, help="Ports to Scan. If not specified standard IANA Ports will be used.")

parser.add_argument( '-openssl',action='store_true', help="Print OpenSSL Commands so testing get can get done with OpenSSL.")
parser.add_argument( '-nmap', action='store_true', help="Use NMAP to scan Domains for ports only. ")

parser.add_argument( '-test', choices=COMMON_MAIL_PROVIDERS, help="Test a common provider such as GMAIL or YAHOO")

args = parser.parse_args()

if args.test is not None:
    testing_common_providers(args.test)

elif args.nmap==True and args.domains is not None and args.openssl==True:
    hosts_with_ports = scan_mail_server_standard_ports(args.domains)
    openssl_commands_from_nmap_scan(hosts_with_ports)

elif args.nmap==True and args.domains is not None:
    hosts_with_ports = scan_mail_server_standard_ports(args.domains)
    print(json.dumps(hosts_with_ports,indent=4))


elif args.openssl==True and args.domains is not None and args.protocols is not None and args.tlssuites is not None:
    openssl_standard_ports_terminal(args.domains,args.protocols,args.tlssuites)

# elif args.openssl==True and args.domains is not None and args.protocols is not None:
#     openssl_standard_ports_terminal(args.domains,args.protocols)
