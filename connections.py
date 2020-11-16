from conversations import decide_protocol_handler
from constants import *

import socket
import ssl
import time


def insecure_connection(HOST,PORT,PROTOCOL="smtp"):
    
    """
    Insecure Connections: This is a standard IPV4 socket
    params:
    HOST - host to connect to - this should be a string
    PORT - port to connect to - this should be an INT
    PROTOCOl - protocol to test - this should be a string
    """
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



def starttls_connection(HOST,PORT,PROTOCOL="smtp",TLSSTRENGTH="tls1_2"):
    """
    STARTTLS Connection: This is a standard IPV4 socket that passes a STARTTLS Commands
    STARTTLS REFERENCE: https://www.fastmail.com/help/technical/ssltlsstarttls.html
    STARTTLS PYTHON WITH SOCKETS CODE: https://stackoverflow.com/questions/12593944/how-to-start-tls-on-an-active-connection-in-python
    THE code above is Python2 ssl so the code below uses SSL contexts compatible with Python3 Sockets and SSL
    NOTE: some protocols such as IMAP and SMTP require extra data to be sent or formatting

    params:
    HOST - host to connect to - this should be a string
    PORT - port to connect to - this should be an INT
    PROTOCOl - protocol to test - this should be a string
    TLSSTRENGTH - in OpenSSL syntax
    """
    print("Connecting to host: {}  on Port Number {} using STARTTLS \r\n".format(HOST,PORT))

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

        client.settimeout(SOCKET_TIMEOUT)
        context = create_tls_context(TLSSTRENGTH)
        try:
            client.connect((HOST, PORT))
            data = client.recv(1024)

            # SMTP NEEDS A EHLO MESSAGE BEFORE STARTTLS AND OTHER COMMANDS
            # IMAP NEEDS A RANDOM STRING FOR THE STARTTLS COMMAND
            # POP3 - investigate but for now assume it's just a straight forward stattls

            if PROTOCOL=="smtp":
                client.send(SMTP_EHLO)
                data = client.recv(1024)
                #print('Received', repr(data))
                client.send(STARTTLS_COMMAND)
                data = client.recv(1024)
                print('Response from STARTTLS_COMMAND:', repr(data))

            if PROTOCOL=="imap":
                client.send(IMAP_RAND_STRING + STARTTLS_COMMAND)
                data = client.recv(1024)
                #print('Response from STARTTLS_COMMAND', repr(data))

            if PROTOCOL=="pop":
                client.send(STARTTLS_COMMAND)
                data = client.recv(1024)
                #print('Response from STARTTLS_COMMAND', repr(data))



            secure_client = context.wrap_socket(client,server_hostname=HOST)

            # SMTP NEEDS A EHLO MESSAGE BEFORE STARTTLS AND OTHER COMMANDS

            if PROTOCOL=="smtp":
                secure_client.send(SMTP_EHLO)
                data = secure_client.recv(1024)
                #print('Results of SMTP EHLO', repr(data),'\r\n')

            #pass the secure client to the write protocol conversation handler
            print_cipher_certificate(secure_client)
            decide_protocol_handler(secure_client,PROTOCOL)

        except Exception as e:
            print("Connection Could Not Be Established \r\n")
            print(e)

def secure_connection(HOST,PORT,PROTOCOL="smtp",TLSSTRENGTH="tls1_2"):
    """
    Secure Connection as per python 3 SSL documentation
    https://docs.python.org/3/library/ssl.html
    We call a method to create the context as we may use different TLS methods

    params:
    HOST - host to connect to - this should be a string
    PORT - port to connect to - this should be an INT
    PROTOCOl - protocol to test - this should be a string
    TLSSTRENGTH - in OpenSSL syntax
    """

    print("Connecting to host: {}  on Port Number {} using an IMPLICITY SECURE Connection \r\n".format(HOST,PORT))

    context = create_tls_context(TLSSTRENGTH)
    secure_client = context.wrap_socket(socket.socket(socket.AF_INET),server_hostname=HOST)
    secure_client.settimeout(SOCKET_TIMEOUT)

    try:
        secure_client.connect((HOST,PORT))
        # SMTP NEEDS A EHLO MESSAGE BEFORE OTHER COMMANDS
        # IMAP AND POP DO NOT
        data = secure_client.recv(1024)
        if PROTOCOL=="smtp":
            secure_client.send(SMTP_EHLO)
            data = secure_client.recv(1024)
            #print('SMTP EHLO RESPONSE: ', repr(data))
        print_cipher_certificate(secure_client)
        decide_protocol_handler(secure_client,PROTOCOL)

    except Exception as e:
        print("Connection Could Not Be Established \r\n")
        print(e)




def print_cipher_certificate(secure_client):
    """
    Method to print certificate and cipher information.
    Pass a Secure Socket Context. Saves having to call this in the various connections methods

    Params:

    secure_client - a secure socket context
    """
    cert = secure_client.getpeercert()
    #print("Ciphers offered to the Mail Server During Negotiations: {}\r\n".format(secure_client.shared_ciphers()))
    print("Cipher in use for this TLS Connection: {} \r\n".format(secure_client.cipher()))
    print("Certificate is Issued By: {} \r\n".format(cert["issuer"]))
    print("Certificate covers the following Domains: {}\r\n".format(cert["subjectAltName"]))



def create_tls_context(TLSSTRENGTH):
    """
    Method to create a TLS context. Gives us flexibility in how we create TLS Sockets.

    Params:

    TLSSTRENGTH - in OpenSSL syntax

    Returns:

    ssl.SSLContext object
    """

    #CREATE a CONTEXT that we can then update
    context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS)

    if TLSSTRENGTH == "tls1_3":
        context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLSv1_3)

    if TLSSTRENGTH == "tls1_2":
        context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLSv1_2)

    elif TLSSTRENGTH == "tls1_1":
        context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLSv1_1)

    elif TLSSTRENGTH == "tls1":
        context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLSv1)

    else:
        print("Valid TLS Protocol Not Found: Needs to be in OpenSSL format: tls_1, tls_1_1 tls_2")
        return

    context.verify_mode = ssl.CERT_REQUIRED
    context.check_hostname = True
    context.load_default_certs()
    print("TLS Protocol Specified: {}".format(TLSSTRENGTH))
    return context
