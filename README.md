# SSL-MAIL-PROTOCOLS-TESTING

A python Script to test SSL configurations on Mail Servers

Analysis and some of the background can be found in this article. https://community.letsencrypt.org/t/tutorial-testing-mail-protocols-with-ssl-tls/43211/11

Usage - the script doesn't take parameters but a couple of example are below

### EXAMPLES:

testing_common_providers is a file that contains test examples for common providers and standard protocols.

######Testing Google Mail Services:

test_gmail_services()

This will run a series of connections on GMAIL services.

Insecure SMTP on Port 25 (this should not allow for authentication as this requires STARTTLS to be run)
SMTP with STARTLS on Port 25
SMTP with STARTLS on Port 587
SMTP over TLS Connection on Port 456

IMAP over TLS Connection on Port 993
POP over TLS Connection on Port 995

######Testing Yahho Mail Services:

test_yahoo_services()

This will test a series of connections on Yahoo services. Yahoo is very similar to Google so we will run the same suite.

# Update the Credential to Valid Credentials

Credentials below should be updated. If credentials are not updated and SSL works you will get error for authentication stage.

It's useful for troubleshooting as it show TLS/SSL transport is working. You won't be able to troubleshoot higher level protocol errors.

> EMAIL_USERNAME = b'changeme@gmail.com'
EMAIL_PASSWORD = b'changeme'


# To Do

A) Test TLS1.2, TLS1.1 and TLS1.0 handshakes automatically for a given server
~B) Test Ports Automatically Given A HOST~
C) Add Argparse for commandline
~D) -Script Output -- allows for openssl commands to be dumpted to screen so users can test with openssl~
E) - Custom Ports -- allow for custom Ports for testing emails
F) Better Error Handling for selecting the wrong Strategy
G) JSON Parsing of Mail Server to Test

# Known Issues

A) Some servers do not return responses as one TCP packet which causes issues when reading results (I should clear the result stream before moving to the next step). This can lead to false Results. Example: mail.zoho.com

# Further Development and No "Issues"

I wrote this script specifically for Let's Encrypt testing as I contribute to the forums.

If you have ideas or suggestions please post them on the Let's Encrypt forum https://community.letsencrypt.org

I suggest adding my tag @ahaw021 so I am made aware of any posts
