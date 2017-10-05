import argparse

from testing_common_providers import *
from testing_private_providers import *
from nmap_scanner import *
from openssl_syntax_output import *
from constants import *

parser = argparse.ArgumentParser(description="Testing Tool for TLS/SSL Protocols for Mail Servers")

parser.add_argument( '--domains', nargs='*', default="smtp.gmail.com", help="Domains to Scan. Multiple Domains can be provided")
parser.add_argument( '-tlssuite', choices=OPENSSL_TLS_SUITES, help="TLS Suite as Per OpenSSL Syntax")
parser.add_argument( '-protocols', choices=MAIL_PROTOCOLS, default="smtp", nargs='*', help="Protools to Scan. This can be one or all 3")
parser.add_argument( '-openssl', help="Print OpenSSL Commands so testing get can get done with OpenSSL.")
parser.add_argument( '-nmap', help="Use NMAP to scan Domains for ports and services. ")
parser.add_argument( '-json', help="Print OpenSSL Commands so testing get can get done with OpenSSL.")
parser.add_argument( '-ports', type=int, nargs='*', help="Ports to Scan. If not specified standard IANA Ports will be used.")

args = parser.parse_args()

print(args.domains)
print(args.protocols)
