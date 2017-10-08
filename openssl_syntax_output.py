from constants import *

"""
Prints out OpenSSL commands for standard IANA ports. Given a host and protocol and TLS Suite the right openssl
commands are printed out to command line.

params:
HOST - host to connect to - this should be a string
PROTOCOl - protocol to test - this should be a string
TLSSTRENGTH - in OpenSSL syntax
"""

def openssl_standard_ports_terminal(HOSTS,PROTOCOLS,TLSSTRENGTH="tls1_2"):
    print("\r\nOpenSSL Commands for Testing -- Printed in Terminal \r\n")
    print("NOTE: To Test Insecure Protocols Use a Client like putty or telnet\r\n")

    for host in HOSTS:
        for protocol in PROTOCOLS:
            if protocol == "pop":
                print("openssl s_client -connect {}:{} -{}".format(host,POP_STANDARD,TLSSTRENGTH))
                print("openssl s_client -connect {}:{} -starttls pop3 -{}".format(host,POP_STANDARD,TLSSTRENGTH))
                print("openssl s_client -connect {}:{} -{}".format(host,POP_IMPLICIT_SSL,TLSSTRENGTH))
                print("openssl s_client -connect {}:{} -starttls pop3 -{}".format(host,POP_IMPLICIT_SSL,TLSSTRENGTH))

            elif protocol == "imap":
                print("openssl s_client -connect {}:{} -{}".format(host,IMAP_STANDARD,TLSSTRENGTH))
                print("openssl s_client -connect {}:{} -starttls imap -{}".format(host,IMAP_STANDARD,TLSSTRENGTH))
                print("openssl s_client -connect {}:{} -{}".format(host,IMAP_IMPLICIT_SSL,TLSSTRENGTH))
                print("openssl s_client -connect {}:{} -starttls imap -{}".format(host,IMAP_IMPLICIT_SSL,TLSSTRENGTH))

            elif protocol == "smtp":
                print("openssl s_client -connect {}:{} -starttls smtp -{}".format(host,SMTP_STANDARD,TLSSTRENGTH))
                print("openssl s_client -connect {}:{} -{}".format(host,SMTP_STARTTLS_SSL,TLSSTRENGTH))
                print("openssl s_client -connect {}:{} -starttls smtp -{}".format(host,SMTP_STARTTLS_SSL,TLSSTRENGTH))
                print("openssl s_client -connect {}:{} -{}".format(host,SMTP_IMPLICIT_SSL,TLSSTRENGTH))

            else:
                print("Protocol Not Found: Valid Options Are: pop, smtp or imap")
            print()
