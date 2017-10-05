from conversations import decide_protocol_handler
from constants import *

import socket
import ssl
import time

def insecure_connection(HOST,PORT,PROTOCOL):
    print("Connecting to host: {}  on Port Number {} using Plaintext \r\n".format(HOST,PORT))
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.settimeout(SOCKET_TIMEOUT)

        try:
            client.connect((HOST, PORT))
            data = client.recv(1024)
            #print('Received', repr(data))

            client.send(SMTP_EHLO)
            data = client.recv(1024)
            #print('Received', repr(data))

            decide_protocol_handler(client,PROTOCOL)

        except:
            print("Connection Could Not Be Established \r\n")
            pass

# STARTTLS REFERENCE: https://www.fastmail.com/help/technical/ssltlsstarttls.html
# STARTTLS PYTHON WITH SOCKETS CODE: https://stackoverflow.com/questions/12593944/how-to-start-tls-on-an-active-connection-in-python
# THE code above is Python2 ssl so the code below uses SSL contexts compatible with Python3 Sockets and SSL

def starttls_connection(HOST,PORT,PROTOCOL,TLSSTRENGTH="tls1_2"):
    print("Connecting to host: {}  on Port Number {} using STARTTLS \r\n".format(HOST,PORT))

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

        client.settimeout(SOCKET_TIMEOUT)

        try:
            client.connect((HOST, PORT))
            data = client.recv(1024)

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

        except:
            print("Connection Could Not Be Established \r\n")
            pass


# Standard SSL Python 3 Code (straight from documents)

def secure_connection(HOST,PORT,PROTOCOL,TLSSTRENGTH="tls1_2"):
    print("Connecting to host: {}  on Port Number {} using an IMPLICITY SECURE Connection \r\n".format(HOST,PORT))
    print("TLS Cipher Suite Selected: {} \r\n".format(TLSSTRENGTH))
    context = ssl.create_default_context()
    secure_client = context.wrap_socket(socket.socket(socket.AF_INET),server_hostname=HOST)
    secure_client.settimeout(SOCKET_TIMEOUT)

    try:
        secure_client.connect((HOST,PORT))
        # SMTP NEEDS A EHLO MESSAGE BEFORE OTHER COMMANDS
        # IMAP AND POP DO NOT
        data = secure_client.recv(1024)
        if PROTOCOL=="SMTP":
            secure_client.send(SMTP_EHLO)
            data = secure_client.recv(1024)
            #print('SMTP EHLO RESPONSE: ', repr(data))
        print_cipher_certificate(secure_client)
        decide_protocol_handler(secure_client,PROTOCOL)

    except Exception as e:
        print("Connection Could Not Be Established \r\n")
        print(e)
        pass


def print_cipher_certificate(secure_client):
    #print("TLS Cipher Suite Selected: {} \r\n".format(TLSSTRENGTH))
    cert = secure_client.getpeercert()
    #print("Ciphers offered to the Mail Server During Negotiations: {}\r\n".format(secure_client.shared_ciphers()))
    print("Cipher in use for this TLS Connection: {} \r\n".format(secure_client.cipher()))
    print("Certificate is Issued By: {} \r\n".format(cert["issuer"]))
    print("Certificate covers the following Domains: {}\r\n".format(cert["subjectAltName"]))


def configure_tls_context(TLSSTRENGTH):

    
    # SET TLS PROTOCOL FOR CONTEXT - a better way would be a dictionary of OPENSSL syntax to python 3

    if TLSSTRENGTH == "tls1_2":
        print("TLS Stength is TLS_1_2")

    elif TLSSTRENGTH == "tls1_2":
        print("TLS Stength is TLS_1_2")

    elif TLSSTRENGTH == "tls1_2":
        print("TLS Stength is TLS_1_2")

    else:
        print("Valid TLS Protocol Not Found: Needs to be in OpenSSL format: tls_1, tls_1_1 tls_2")
