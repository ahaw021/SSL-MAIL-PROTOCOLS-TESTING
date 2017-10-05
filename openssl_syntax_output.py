from constants import *

def openssl_standard_ports_terminal(URL="imap.google.com",PROTOCOL="imap",TLSSTRENGTH="tls1_2"):
    print("OpenSSL Commands for Testing -- Printed in Terminal \r\n")
    print("NOTE: To Test Insecure Protocols Use a Client like putty or telnet")

    if PROTOCOL == "POP":
        print("openssl s_client -connect {}:{} -{}".format(URL,POP_STANDARD,TLSSTRENGTH))
        print("openssl s_client -connect {}:{} -starttls pop3 -{}".format(URL,POP_STANDARD,TLSSTRENGTH))
        print("openssl s_client -connect {}:{} -{}".format(URL,POP_IMPLICIT_SSL,TLSSTRENGTH))
        print("openssl s_client -connect {}:{} -starttls pop3 -{}".format(URL,POP_IMPLICIT_SSL,TLSSTRENGTH))

    elif PROTOCOL == "IMAP":
        print("openssl s_client -connect {}:{} -{}".format(URL,IMAP_STANDARD,TLSSTRENGTH))
        print("openssl s_client -connect {}:{} -starttls imap -{}".format(URL,IMAP_STANDARD,TLSSTRENGTH))
        print("openssl s_client -connect {}:{} -{}".format(URL,IMAP_IMPLICIT_SSL,TLSSTRENGTH))
        print("openssl s_client -connect {}:{} -starttls imap -{}".format(URL,IMAP_IMPLICIT_SSL,TLSSTRENGTH))

    elif PROTOCOL == "SMTP":
        print("openssl s_client -connect {}:{} -starttls smtp -{}".format(URL,SMTP_STANDARD,TLSSTRENGTH))
        print("openssl s_client -connect {}:{} -{}".format(URL,SMTP_STARTTLS_SSL,TLSSTRENGTH))
        print("openssl s_client -connect {}:{} -starttls smtp -{}".format(URL,SMTP_STARTTLS_SSL,TLSSTRENGTH))
        print("openssl s_client -connect {}:{} -{}".format(URL,SMTP_IMPLICIT_SSL,TLSSTRENGTH))

    else:
        print("Protocol Not Found: Valid Options Are: POP, SMTP or IMAP")

def openssl_standard_ports_file(url="imap.google.com",protocol="imap"):
    print("OpenSSL to File")
