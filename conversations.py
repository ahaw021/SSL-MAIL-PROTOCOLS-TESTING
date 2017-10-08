from constants import *
import base64

"""
Function to decide what conversation based on protocol. As each protocol has a different syntax we need this function to point to the right function.
params:
client - a python Socket Client - can be secure on insecure (conversations don't care about transport)
PROTOCOl - protocol to test - this should be a string
"""

def decide_protocol_handler(client, PROTOCOL):
    if PROTOCOL=="smtp":
        smtp_conversation(client)

    elif PROTOCOL=="pop":
        pop_conversation(client)

    elif PROTOCOL=="imap":
        imap_conversation(client)

    else:
        print("NOT A KNOWN PROTOCOL --- BYEEE")

"""
Function to test that POP service is responding as expected
POP COMMAND REFERENCE: https://blog.yimingliu.com/2009/01/23/testing-a-pop3-server-via-telnet-or-openssl/
Currently working to Authentication only - no email is sent

params:

client - a python Socket Client - can be secure on insecure (conversations don't care about transport)

"""

def pop_conversation(client):
    print("Let's Start a POP Conversation: \r\n")

    print("Username formatted for POP: {}".format(POP_USER + EMAIL_USERNAME + b' \r\n'))
    client.send(POP_USER + EMAIL_USERNAME + b' \r\n')
    data = client.recv(1024)
    print(data)

    print("Password formatted for POP: {}".format(POP_PASS + EMAIL_PASSWORD + b' \r\n'))
    client.send(POP_PASS + EMAIL_PASSWORD + b' \r\n')
    data = client.recv(1024)
    print(data)

"""
Function to test that SMTP service is responding as expected
SMTP COMMAND REFERENCE: https://www.ndchost.com/wiki/mail/test-smtp-auth-telnet
Currently working to Authentication only - no email is sent

params:

client - a python Socket Client - can be secure on insecure (conversations don't care about transport)

"""

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

"""
Function to test that IMAP service is responding as expected
IMAP COMMAND REFERENCE: http://busylog.net/telnet-imap-commands-note/
Currently working to Authentication only - no email is sent

params:

client - a python Socket Client - can be secure on insecure (conversations don't care about transport)

"""

def imap_conversation(client):
    print("Let's Start an IMAP Conversation: \r\n")

    print("Authentication String: {}".format(IMAP_RAND_STRING + IMAP_LOGIN + EMAIL_USERNAME +b' ' + EMAIL_PASSWORD + b' \r\n'))
    client.send(IMAP_RAND_STRING + IMAP_LOGIN + EMAIL_USERNAME +b' ' + EMAIL_PASSWORD + b'\r\n')
    data = client.recv(1024)
    print(data)
