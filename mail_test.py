import json
from testing_common_providers import *
from nmap_scanner import *
STARTTLS_COMMAND = b'STARTTLS \r\n'
import argparse

EMAIL_USERNAME = b'changeme@gmail.com'
EMAIL_PASSWORD = b'changeme'

test_gmail_services()
