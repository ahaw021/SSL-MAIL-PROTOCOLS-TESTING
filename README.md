# SSL-MAIL-PROTOCOLS-TESTING

A python Script to test SSL configurations on Mail Servers

Analysis and some of the background can be found in this article. https://community.letsencrypt.org/t/tutorial-testing-mail-protocols-with-ssl-tls/43211/11

Usage - the script doesn't take parameters but a couple of example are below

### EXAMPLES:

### Connect to Google SMTP Server via SSL/TLS on 456 and also via STARTTLS on Port 25 and 587

> secure_connection("smtp.gmail.com",SMTP_IMPLICIT_SSL,"SMTP")
starttls_connection("smtp.gmail.com",SMTP_STARTTLS_SSL,"SMTP")
starttls_connection("smtp.gmail.com",SMTP_STANDARD,"SMTP")

### Connect to Google POP and IMAP Server via SSL/TLS on 993 and 995. Google does not have a STARTTLS IMAP or POP Service.

> secure_connection("imap.gmail.com",IMAP_IMPLICIT_SSL,"IMAP")
secure_connection("pop.gmail.com",POP_IMPLICIT_SSL,"POP")

# Update the Credential to Valid Credentials

Credentials below should be updated. If credentials are not updated and SSL works you will get error for authentication stage.

It's useful for troubleshooting as it show TLS/SSL transport is working. You won't be able to troubleshoot higher level protocol errors.

> EMAIL_USERNAME = b'changeme@gmail.com'
EMAIL_PASSWORD = b'changeme'


# To Do

~A) Test TLS1.2, TLS1.1 and TLS1.0 handshakes automatically for a given server~
B) Test Ports Automatically Given A HOST
C) Add Argparse for commandline
D) -Script Output -- allows for openssl commands to be dumpted to screen so users can test with openssl
E) - Custom Ports -- allow for custom Ports for testing emails
F) Better Error Handling for selecting the wrong Strategy

# Known Issues

A) Some servers do not return responses as one TCP packet which causes issues when reading results (I should clear the result stream before moving to the next step). This can lead to false Results. Example: mail.zoho.com

# Further Development and No "Issues"

I wrote this script specifically for Let's Encrypt testing as I contribute to the forums.

If you have ideas or suggestions please post them on the Let's Encrypt forum https://community.letsencrypt.org

I suggest adding my tag @ahaw021 so I am made aware of any posts
