from constants import *

OPENSSL_IMPLICITLY_SECURE = "openssl s_client -connect {}:{} -servername {} -{}"
OPENSSL_STARTTLS_REQUIRED = "openssl s_client -connect {}:{} -servername {} -starttls {} -{}"


def openssl_standard_ports_terminal(HOSTS,PROTOCOLS,TLSSTRENGTH):
    """
    Prints out OpenSSL commands for standard IANA ports. Given a host and protocol and TLS Suite the right openssl
    commands are printed out to command line.

    params:
    HOST - host to connect to - this should be a string
    PROTOCOl - protocol to test - this should be a string
    TLSSTRENGTH - in OpenSSL syntax
    """
    print("\r\nOpenSSL Commands for Testing -- Printed in Terminal \r\n")
    print("NOTE: To Test Insecure Protocols Use a Client like putty or telnet\r\n")

    for host in HOSTS:
        for protocol in PROTOCOLS:
            if protocol == "pop":
                print("openssl s_client -connect {}:{} -servername {} -{}".format(host,POP_STANDARD,host,TLSSTRENGTH))
                print("openssl s_client -connect {}:{} -servername {} -starttls pop3 -{}".format(host,POP_STANDARD,host,TLSSTRENGTH))
                print("openssl s_client -connect {}:{} -servername {} -{}".format(host,POP_IMPLICIT_SSL,host,TLSSTRENGTH))
                print("openssl s_client -connect {}:{} -servername {} -starttls pop3 -{}".format(host,POP_IMPLICIT_SSL,host,TLSSTRENGTH))

            elif protocol == "imap":
                print("openssl s_client -connect {}:{} -servername {} -{}".format(host,IMAP_STANDARD,host,TLSSTRENGTH))
                print("openssl s_client -connect {}:{} -servername {} -starttls imap -{}".format(host,IMAP_STANDARD,host,TLSSTRENGTH))
                print("openssl s_client -connect {}:{} -servername {} -{}".format(host,IMAP_IMPLICIT_SSL,host,TLSSTRENGTH))
                print("openssl s_client -connect {}:{} -servername {} -starttls imap -{}".format(host,IMAP_IMPLICIT_SSL,host,TLSSTRENGTH))

            elif protocol == "smtp":
                print("openssl s_client -connect {}:{} -servername {} -starttls smtp -{}".format(host,SMTP_STANDARD,host,TLSSTRENGTH))
                print("openssl s_client -connect {}:{} -servername {} -{}".format(host,SMTP_STARTTLS_SSL,host,TLSSTRENGTH))
                print("openssl s_client -connect {}:{} -servername {} -starttls smtp -{}".format(host,SMTP_STARTTLS_SSL,host,TLSSTRENGTH))
                print("openssl s_client -connect {}:{} -servername {} -{}".format(host,SMTP_IMPLICIT_SSL,host,TLSSTRENGTH))

            else:
                print("Protocol Not Found: Valid Options Are: pop, smtp or imap")
            print()

def openssl_commands_from_nmap_scan(hosts_with_ports):
    for host in hosts_with_ports:
        for port_to_analyze in host.get("open_mail_ports"):
            generate_open_ssl_command_for_protol(host.get("hostname"),port_to_analyze)

def generate_open_ssl_command_for_protol(hostname,port_to_analyze,tls_suite="tls1_2"):
    print(OPENSSL_IMPLICITLY_SECURE.format(hostname,port_to_analyze.get("port"),hostname,tls_suite))
    print(OPENSSL_STARTTLS_REQUIRED.format(hostname,port_to_analyze.get("port"),hostname,port_to_analyze.get("protocol"), tls_suite))


