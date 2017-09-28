import socket
import ssl
import base64
import json
import time

#don't forget \r\n on commands otherwise they won't get submitted to the server (sent but no response will come back)
# these should probably be broken out in to a separate dictionary file but here for now


with open('mail_servers.json') as data_file:
    TEST_SERVERS = json.load(data_file)

POP_STANDARD = 110
POP_IMPLICIT_SSL = 995
POP_USER = b'USER \r\n'
POP_PASS = b'PASS \r\n'

SMTP_STANDARD = 25
SMTP_IMPLICIT_SSL = 465
SMTP_STARTTLS_SSL = 587
SMTP_EHLO = b'EHLO gmail.com \r\n'
SMTP_AUTH = b'AUTH LOGIN \r\n'

IMAP_STANDARD = 143
IMAP_IMPLICIT_SSL = 993
IMAP_RAND_STRING = b'A1'
IMAP_CAPABILITY = b'CAPABILITY \r\n'
IMAP_LOGIN = b'LOGIN '

STARTTLS_COMMAND = b'STARTTLS \r\n'

EMAIL_USERNAME = b''
EMAIL_PASSWORD = b''



def insecure_connection(HOST,PORT,PROTOCOL):
    print('Connecting to host: {}  on Port Number {} using Plaintext'.format(HOST,PORT))
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        data = client.recv(1024)
        #print('Received', repr(data))

        client.send(SMTP_EHLO)
        data = client.recv(1024)
        #print('Received', repr(data))

        decide_protocol_handler(client,PROTOCOL)


# STARTTLS REFERENCE: https://www.fastmail.com/help/technical/ssltlsstarttls.html
# STARTTLS PYTHON WITH SOCKETS CODE: https://stackoverflow.com/questions/12593944/how-to-start-tls-on-an-active-connection-in-python
# THE code above is Python2 ssl so the code below uses SSL contexts compatible with Python3 Sockets and SSL

def starttls_connection(HOST,PORT,PROTOCOL):
    print('Connecting to host: {}  on Port Number {} using STARTTLS'.format(HOST,PORT))
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

        client.connect((HOST, PORT))
        data = client.recv(1024)
        #print('Received', repr(data))

        client.send(SMTP_EHLO)
        data = client.recv(1024)
        #print('Received', repr(data))

        client.send(STARTTLS_COMMAND)
        data = client.recv(1024)
        #print('Received', repr(data))

        context = ssl.create_default_context()
        secure_client = context.wrap_socket(client,server_hostname=HOST)
        secure_client.send(SMTP_EHLO)
        data = secure_client.recv(1024)
        print('Received', repr(data),'\r\n')

        cert = secure_client.getpeercert()
        print("Certificate is Issued By: {} \r\n".format(cert["issuer"]))
        print("Certificate covers the following Domains: {}\r\n".format(cert["subjectAltName"]))

        #pass the secure client to the write protocol conversation handler

        decide_protocol_handler(secure_client,PROTOCOL)

# Standard SSL Python 3 Code (straight from documents)

def secure_connection(HOST,PORT,PROTOCOL):

    context = ssl.create_default_context()
    secure_client = context.wrap_socket(socket.socket(socket.AF_INET),server_hostname=HOST)
    secure_client.connect((HOST,PORT))

    secure_client.send(SMTP_EHLO)
    data = secure_client.recv(1024)
    print('Received', repr(data),'\r\n')

    cert = secure_client.getpeercert()
    print("Certificate is Issued By: {} \r\n".format(cert["issuer"][2]))
    print("Certificate covers the following Domains: {}\r\n".format(cert["subjectAltName"]))

    decide_protocol_handler(secure_client,PROTOCOL)

def decide_protocol_handler(client, PROTOCOL):
    if PROTOCOL=="SMTP":
        smtp_conversation(client)

    elif PROTOCOL=="POP":
        pop_conversation(client)

    elif PROTOCOL=="IMAP":
        imap_conversation(client)

    else:
        print("NOT A KNOWN PROTOCOL --- BYEEE")

# these methods actually pass data back and forwards to the server to confirm server functioning
# POP COMMAND REFERENCE: https://blog.yimingliu.com/2009/01/23/testing-a-pop3-server-via-telnet-or-openssl/
# SMTP COMMAND REFERENCE: https://www.ndchost.com/wiki/mail/test-smtp-auth-telnet
# IMAP COMMAND REFERENCE: http://busylog.net/telnet-imap-commands-note/


def pop_conversation(socket):
    print("Let's Start a POP Conversation: \r\n")

def smtp_conversation(socket):
    print("Let's Start an SMTP Conversation: \r\n")

def imap_conversation(socket):
    print("Let's Start an IMAP Conversation: \r\n")

#EXAMPLES:

# secure_connection("smtp.gmail.com",SMTP_IMPLICIT_SSL,"SMTP")
# starttls_connection("smtp.gmail.com",SMTP_STARTTLS_SSL,"SMTP")
