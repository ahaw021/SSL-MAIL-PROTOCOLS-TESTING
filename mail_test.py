import json
import argparse

from testing_common_providers import *
from nmap_scanner import *
from openssl_syntax_output import *

scan_mail_server_standard_ports("smtp.gmail.com")
scan_mail_server_standard_ports_services("smtp.gmail.com")
