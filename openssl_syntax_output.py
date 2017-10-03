from constants import *

def openssl_standard_ports_terminal(URL="imap.google.com",PROTOCOL="imap"):
    print("OpenSSL Commands for Testing -- Printed in Terminal \r\n")

    if PROTOCOL == "POP":
        print("openssl s_client -connect {}:{}".format(URL,POP_STANDARD))
        print("openssl s_client -connect {}:{} -starttls pop3".format(URL,POP_STANDARD))
        print("openssl s_client -connect {}:{}".format(URL,POP_IMPLICIT_SSL))
        print("openssl s_client -connect {}:{} -starttls pop3".format(URL,POP_IMPLICIT_SSL))

    elif PROTOCOL == "IMAP":
        print("openssl s_client -connect {}:{}".format(URL,IMAP_STANDARD))
        print("openssl s_client -connect {}:{} -starttls imap".format(URL,IMAP_STANDARD))
        print("openssl s_client -connect {}:{}".format(URL,IMAP_IMPLICIT_SSL))
        print("openssl s_client -connect {}:{} -starttls imap".format(URL,IMAP_IMPLICIT_SSL))

    elif PROTOCOL == "SMTP":
        print("openssl s_client -connect {}:{} -starttls smtp".format(URL,SMTP_STANDARD))
        print("openssl s_client -connect {}:{}".format(URL,SMTP_IMPLICIT_SSL))
        print("openssl s_client -connect {}:{} ".format(URL,SMTP_STARTTLS_SSL))
        print("openssl s_client -connect {}:{} -starttls smtp".format(URL,SMTP_STARTTLS_SSL))

    else:
        print("Protocol Not Found: Valid Options Are: POP, SMTP or IMAP")

def openssl_standard_ports_file(url="imap.google.com",protocol="imap"):
    print("OpenSSL to File")
