import socket
import ssl
import base64
import json
import time
import os

#don't forget \r\n on commands otherwise they won't get submitted to the server (sent but no response will come back)
# these should probably be broken out in to a separate dictionary file but here for now


with open('mail_servers.json') as data_file:
    TEST_SERVERS = json.load(data_file)

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

EMAIL_USERNAME = b'changeme@gmail.com'
EMAIL_PASSWORD = b'changeme'



def insecure_connection(HOST,PORT,PROTOCOL):
    print('Connecting to host: {}  on Port Number {} using Plaintext \r\n'.format(HOST,PORT))
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

def starttls_connection(HOST,PORT,PROTOCOL,TLSSTRENGTH):
    print('Connecting to host: {}  on Port Number {} using STARTTLS \r\n'.format(HOST,PORT))
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

        client.connect((HOST, PORT))
        data = client.recv(1024)
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

        cert = secure_client.getpeercert()
        print("Certificate is Issued By: {} \r\n".format(cert["issuer"]))
        print("Certificate covers the following Domains: {}\r\n".format(cert["subjectAltName"]))


        print("Cipher in use for this TLS Connection: {} \r\n".format(secure_client.cipher()))
        #print("Ciphers offered to the Mail Server During Negotiations: {}\r\n".format(secure_client.shared_ciphers()))


        #pass the secure client to the write protocol conversation handler

        decide_protocol_handler(secure_client,PROTOCOL)



# Standard SSL Python 3 Code (straight from documents)

def secure_connection(HOST,PORT,PROTOCOL,TLSSTRENGTH):
    print('Connecting to host: {}  on Port Number {} using an IMPLICITY SECURE Connection \r\n'.format(HOST,PORT))
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


    cert = secure_client.getpeercert()
    print("Certificate is Issued By: {} \r\n".format(cert["issuer"]))
    print("Certificate covers the following Domains: {}\r\n".format(cert["subjectAltName"]))

    decide_protocol_handler(secure_client,PROTOCOL)

# Function for choosing conversation path based on Protocol

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
# Currently working to Authentication only


def pop_conversation(client):
    print("Let's Start a POP Conversation: \r\n")

    time.sleep(1)
    print("Username formatted for POP: {}".format(POP_USER + EMAIL_USERNAME + b' \r\n'))
    client.send(POP_USER + EMAIL_USERNAME + b' \r\n')
    data = client.recv(1024)
    print(data)

    print("Password formatted for POP: {}".format(POP_PASS + EMAIL_PASSWORD + b' \r\n'))
    client.send(POP_PASS + EMAIL_PASSWORD + b' \r\n')
    data = client.recv(1024)
    print(data)


def smtp_conversation(client):

    print("Let's Start an SMTP Conversation: \r\n")
    client.send(SMTP_AUTH)
    data = client.recv(1024)

    b64_encoded = base64.b64encode(EMAIL_USERNAME)
    print("Username Encoded as base64: {}".format(b64_encoded))
    client.send(b64_encoded)
    client.send(b'\r\n')
    data = client.recv(1024)
    #print("Server After Username: {}".format(data))

    b64_encoded = base64.b64encode(EMAIL_PASSWORD)
    print("Password Encoded as base64: {}\r\n".format(b64_encoded))
    client.send(b64_encoded)
    client.send(b'\r\n')
    data = client.recv(1024)
    print("Server Response: {}".format(data))

def imap_conversation(client):
    print("Let's Start an IMAP Conversation: \r\n")

    print("Authentication String: {}".format(IMAP_RAND_STRING + IMAP_LOGIN + EMAIL_USERNAME +b' ' + EMAIL_PASSWORD + b' \r\n'))
    client.send(IMAP_RAND_STRING + IMAP_LOGIN + EMAIL_USERNAME +b' ' + EMAIL_PASSWORD + b'\r\n')
    data = client.recv(1024)
    print(data)



#EXAMPLES:

#starttls_connection("smtp.gmail.com",SMTP_STARTTLS_SSL,"SMTP","TLS1")
#starttls_connection("smtp.gmail.com",SMTP_STANDARD,"SMTP","TLS1")

#starttls_connection("smtp.mail.yahoo.com",SMTP_STARTTLS_SSL,"SMTP","TLS1")
#starttls_connection("smtp.mail.yahoo.com",SMTP_STANDARD,"SMTP","TLS1")
#secure_connection("smtp.yahoo.com",SMTP_IMPLICIT_SSL,"SMTP","TLS1")

#starttls_connection("mx3.hotmail.com",SMTP_STANDARD,"SMTP","TLS1")

#secure_connection("imap.gmail.com",IMAP_IMPLICIT_SSL,"IMAP","TLS1")
#secure_connection("pop.gmail.com",POP_IMPLICIT_SSL,"POP","TLS1")

#secure_connection("imap.mail.yahoo.com",IMAP_IMPLICIT_SSL,"IMAP","TLS1")
#secure_connection("pop.mail.yahoo.com",POP_IMPLICIT_SSL,"POP","TLS1")
