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
