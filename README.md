# SSL-MAIL-PROTOCOLS-TESTING

A python Script to test SSL configurations on Mail Servers

Analysis and some of the background can be found in this article. https://community.letsencrypt.org/t/tutorial-testing-mail-protocols-with-ssl-tls/43211/11

mail-test.py -h

-domains [DOMAINS [DOMAINS ...]]
                      Domains to Scan. Multiple Domains can be provided

-tlssuite {tls1,tls1_1,tls1_2}
                      TLS Suite as Per OpenSSL Syntax. If not specific TLS
                      1.2 will be used.

-protocols [{smtp,pop,imap} [{smtp,pop,imap} ...]]
                      Protools to Scan. This can be one or all 3. If not specified SMTP will be tested

-ports [PORTS [PORTS ...]]
                      Ports to Scan. If not specified standard IANA Ports
                      will be used.

-openssl              Print OpenSSL Commands so testing get can get done
                      with OpenSSL.

-nmap                 Use NMAP to scan Domains for ports only.

-nmapservices         Use NMAP to scan Domains for ports and service
                      Identification.

-test {gmail,yahoo,hotmail,zoho}
                      Test a common provider such as GMAIL or YAHOO
                      

## EXAMPLES:

Some common examples are below

####Testing Google Mail Services:

>mail-test.py -test gmail

This will run a series of connections on GMAIL services.

Insecure SMTP on Port 25 (this should not allow for authentication as this requires STARTTLS to be run)
SMTP with STARTLS on Port 25
SMTP with STARTLS on Port 587
SMTP over TLS Connection on Port 456

IMAP over TLS Connection on Port 993
POP over TLS Connection on Port 995

#### Use Nmap to identify open ports:

>mail-test -domains smtp.gmail.com imap.gmail.com -nmap

#### Use Nmap to identify open ports and mail server version:

>mail-test -domains smtp.gmail.com imap.gmail.com -nmapservices

#### Create OpenSSL Commands to Test with OpenSSL:

>mail-test -domains smtp.gmail.com imap.gmail.com -protocols imap smtp -openssl

#### Create OpenSSL Commands to Test with OpenSSL for a specific TLS Suite:

>mail-test -domains smtp.gmail.com imap.gmail.com -tlssuite tls1_1 -protocols imap smtp -openssl

## CREDENTIALS:

Credentials in constant.py should be updated. If credentials are not updated and SSL works you will get error for authentication stage.

It's useful for troubleshooting as it show TLS/SSL transport is working. You won't be able to troubleshoot higher level protocol errors.

> EMAIL_USERNAME = b'changeme@gmail.com'
EMAIL_PASSWORD = b'changeme'


# To Do

~A) Test TLS1.2, TLS1.1 and TLS1.0 handshakes automatically for a given server~

~B) Test Ports Automatically Given A HOST~

~C) Add Argparse for commandline~

~D) -Script Output -- allows for openssl commands to be dumpted to screen so users can test with openssl~

~E) - Custom Ports -- allow for custom Ports for testing emails~

~F) Better Error Handling for selecting the wrong Strategy~

~G) JSON Parsing of Mail Server to Test~

H) Generic Testing of Protocol Suites. Update Specific providers to use this as well.

# Known Issues

A) Some servers do not return responses as one TCP packet which causes issues when reading results (I should clear the result stream before moving to the next step). This can lead to false Results. Example: mail.zoho.com

# Further Development and No "Issues"

I wrote this script specifically for Let's Encrypt testing as I contribute to the forums.

If you have ideas or suggestions please post them on the Let's Encrypt forum https://community.letsencrypt.org

I suggest adding my tag @ahaw021 so I am made aware of any posts
