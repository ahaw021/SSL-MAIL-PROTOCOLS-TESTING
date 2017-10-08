import argparse

from testing_providers import *
from nmap_scanner import *
from openssl_syntax_output import *
from constants import *
from connections import *

parser = argparse.ArgumentParser(description="Testing Tool for TLS/SSL Protocols for Mail Servers")

parser.add_argument( '-domains', nargs='*', default="smtp.gmail.com", help="Domains to Scan. Multiple Domains can be provided")
parser.add_argument( '-tlssuite',nargs=1, choices=OPENSSL_TLS_SUITES, help="TLS Suite as Per OpenSSL Syntax. If not specific TLS 1.2 will be used. ")
parser.add_argument( '-protocols', choices=MAIL_PROTOCOLS, default="smtp", nargs='*', help="Protools to Scan. This can be one or all 3")
parser.add_argument( '-ports', type=int, nargs='*', default=COMMON_MAIL_PORTS, help="Ports to Scan. If not specified standard IANA Ports will be used.")
parser.add_argument( '-openssl',action='store_true', help="Print OpenSSL Commands so testing get can get done with OpenSSL.")
parser.add_argument( '-nmap', action='store_true', help="Use NMAP to scan Domains for ports only. ")
parser.add_argument( '-nmapservices',action='store_true', help="Use NMAP to scan Domains for ports and service Identification. ")
parser.add_argument( '-test', choices=COMMON_MAIL_PROVIDERS, help="Test a common provider such as GMAIL or YAHOO")

args = parser.parse_args()

if args.test is not None:
    testing_common_providers(args.test)

elif args.nmap==True and args.domains is not None:
    scan_mail_server_standard_ports(args.domains)

elif args.nmapservices==True and args.domains is not None:
    scan_mail_server_standard_ports_services(args.domains)

elif args.openssl==True and args.domains is not None and args.protocols is not None and args.tlssuite is not None:
    print("With TLS Suites")
    openssl_standard_ports_terminal(args.domains,args.protocols,args.tlssuite[0])

elif args.openssl==True and args.domains is not None and args.protocols is not None:
    openssl_standard_ports_terminal(args.domains,args.protocols)
