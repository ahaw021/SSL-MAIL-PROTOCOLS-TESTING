import json

from constants import *
from connections import *

def testing_common_providers(provider):
    if provider == "gmail":
        insecure_connection("smtp.gmail.com",SMTP_STANDARD,"smtp")
        starttls_connection("smtp.gmail.com",SMTP_STANDARD,"smtp")
        insecure_connection("smtp.gmail.com",SMTP_STARTTLS_SSL,"smtp")
        starttls_connection("smtp.gmail.com",SMTP_STARTTLS_SSL,"smtp")
        secure_connection("smtp.gmail.com",SMTP_IMPLICIT_SSL,"smtp")

        secure_connection("imap.gmail.com",IMAP_IMPLICIT_SSL,"imap")
        secure_connection("pop.gmail.com",POP_IMPLICIT_SSL,"pop")

    if provider == "yahoo":
        starttls_connection("smtp.mail.yahoo.com",SMTP_STARTTLS_SSL,"smtp")
        starttls_connection("smtp.mail.yahoo.com",SMTP_STANDARD,"smtp")
        secure_connection("smtp.yahoo.com",SMTP_IMPLICIT_SSL,"smtp")

        secure_connection("imap.mail.yahoo.com",IMAP_IMPLICIT_SSL,"imap")
        secure_connection("pop.mail.yahoo.com",POP_IMPLICIT_SSL,"pop")

    if provider == "hotmail":
        starttls_connection("mx3.hotmail.com",SMTP_STANDARD,"smtp")

    if provider == "zoho":
        starttls_connection("smtp.zoho.com",SMTP_STARTTLS_SSL,"smtp")
        secure_connection("imap.zoho.com",IMAP_IMPLICIT_SSL,"imap")
        secure_connection("pop.zoho.com",POP_IMPLICIT_SSL,"pop")
