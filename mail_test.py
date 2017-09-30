import json
from connections import *
from nmap_scanner import *

POP_STANDARD = 110
POP_IMPLICIT_SSL = 995
POP_USER = b'USER '
POP_PASS = b'PASS '

SMTP_STANDARD = 25
SMTP_IMPLICIT_SSL = 465
SMTP_STARTTLS_SSL = 587
SMTP_EHLO = b'EHLO gmail.com \r\n'
SMTP_AUTH = b'AUTH LOGIN \r\n'

IMAP_STANDARD = 143
IMAP_IMPLICIT_SSL = 993
IMAP_RAND_STRING = b'A1 '
IMAP_CAPABILITY = b'CAPABILITY \r\n'
IMAP_LOGIN = b'LOGIN '

STARTTLS_COMMAND = b'STARTTLS \r\n'

#don't forget \r\n on commands otherwise they won't get submitted to the server (sent but no response will come back)
# these should probably be broken out in to a separate dictionary file but here for now

with open('mail_servers.json') as data_file:
    TEST_SERVERS = json.load(data_file)

global EMAIL_USERNAME
global EMAIL_PASSWORD

EMAIL_USERNAME = b'changeme@gmail.com'
EMAIL_PASSWORD = b'changeme'

scan_mail_server()
