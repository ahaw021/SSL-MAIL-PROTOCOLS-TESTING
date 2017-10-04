from conversations import decide_protocol_handler
from constants import *

import socket
import ssl
import time

def insecure_connection(HOST,PORT,PROTOCOL):
    print("Connecting to host: {}  on Port Number {} using Plaintext \r\n".format(HOST,PORT))
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        try:
            client.connect((HOST, PORT))
        except e:
            print("Connection Could Not Be Established")


        data = client.recv(1024)
        #print('Received', repr(data))

        client.send(SMTP_EHLO)
        data = client.recv(1024)
        #print('Received', repr(data))

        decide_protocol_handler(client,PROTOCOL)


# STARTTLS REFERENCE: https://www.fastmail.com/help/technical/ssltlsstarttls.html
# STARTTLS PYTHON WITH SOCKETS CODE: https://stackoverflow.com/questions/12593944/how-to-start-tls-on-an-active-connection-in-python
# THE code above is Python2 ssl so the code below uses SSL contexts compatible with Python3 Sockets and SSL

def starttls_connection(HOST,PORT,PROTOCOL,TLSSTRENGTH="1.2"):
    print("Connecting to host: {}  on Port Number {} using STARTTLS \r\n".format(HOST,PORT))
    print("TLS Cipher Suite Selected: {} \r\n".format(TLSSTRENGTH))

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

        try:
            client.connect((HOST, PORT))
            data = client.recv(1024)

        except e:
            print("Connection Could Not Be Established")

        #print('Received', repr(data))

        # SMTP NEEDS A EHLO MESSAGE BEFORE STARTTLS AND OTHER COMMANDS
        # IMAP NEEDS A RANDOM STRING FOR THE STARTTLS COMMAND
        # POP3 - investigate but for now assume it's just a straight forward stattls

        if PROTOCOL=="SMTP":
            client.send(SMTP_EHLO)
            data = client.recv(1024)
            #print('Received', repr(data))
            client.send(STARTTLS_COMMAND)
            data = client.recv(1024)
            print('Response from STARTTLS_COMMAND:', repr(data))

        if PROTOCOL=="IMAP":
            client.send(IMAP_RAND_STRING + STARTTLS_COMMAND)
            data = client.recv(1024)
            #print('Response from STARTTLS_COMMAND', repr(data))

        if PROTOCOL=="POP":
            client.send(STARTTLS_COMMAND)
            data = client.recv(1024)
            #print('Response from STARTTLS_COMMAND', repr(data))


        context = ssl.create_default_context()
        secure_client = context.wrap_socket(client,server_hostname=HOST)

        # SMTP NEEDS A EHLO MESSAGE BEFORE STARTTLS AND OTHER COMMANDS

        if PROTOCOL=="SMTP":
            secure_client.send(SMTP_EHLO)
            data = secure_client.recv(1024)
            #print('Results of SMTP EHLO', repr(data),'\r\n')

        #pass the secure client to the write protocol conversation handler
        print_cipher_certificate(secure_client)
        decide_protocol_handler(secure_client,PROTOCOL)

# Standard SSL Python 3 Code (straight from documents)

def secure_connection(HOST,PORT,PROTOCOL,TLSSTRENGTH="1.2"):
    print("Connecting to host: {}  on Port Number {} using an IMPLICITY SECURE Connection \r\n".format(HOST,PORT))
    print("TLS Cipher Suite Selected: {} \r\n".format(TLSSTRENGTH))
    context = ssl.create_default_context()
    secure_client = context.wrap_socket(socket.socket(socket.AF_INET),server_hostname=HOST)
    secure_client.connect((HOST,PORT))
    data = secure_client.recv(1024)

    # SMTP NEEDS A EHLO MESSAGE BEFORE OTHER COMMANDS
    # IMAP AND POP DO NOT

    if PROTOCOL=="SMTP":
        secure_client.send(SMTP_EHLO)
        data = secure_client.recv(1024)
        #print('SMTP EHLO RESPONSE: ', repr(data))
    print_cipher_certificate(secure_client)
    decide_protocol_handler(secure_client,PROTOCOL)

def print_cipher_certificate(secure_client):
    cert = secure_client.getpeercert()
    print("Cipher SUITE SPECIFIED: {} \r\n".format(secure_client))
    print("Ciphers offered to the Mail Server During Negotiations: {}\r\n".format(secure_client.shared_ciphers()))
    print("Cipher in use for this TLS Connection: {} \r\n".format(secure_client.cipher()))
    print("Certificate is Issued By: {} \r\n".format(cert["issuer"]))
    print("Certificate covers the following Domains: {}\r\n".format(cert["subjectAltName"]))
