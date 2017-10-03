import json
import argparse

from testing_common_providers import *
from nmap_scanner import *
from openssl_syntax_output import *

EMAIL_USERNAME = b'changeme@gmail.com'
EMAIL_PASSWORD = b'changeme'

openssl_standard_ports_terminal("imap.zoho.com","IMAP")
openssl_standard_ports_terminal("pop.gmail.com","POP")
openssl_standard_ports_terminal("smtp.hotmail.com","SMTP")
openssl_standard_ports_terminal("xmpp.facebooke.com","XMPP")
