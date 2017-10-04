from constants import *

from connections import *

def test_gmail_services():
    insecure_connection("smtp.gmail.com",SMTP_STARTTLS_SSL,"SMTP")
    starttls_connection("smtp.gmail.com",SMTP_STARTTLS_SSL,"SMTP")
    starttls_connection("smtp.gmail.com",SMTP_STANDARD,"SMTP")
    secure_connection("smtp.gmail.com",SMTP_IMPLICIT_SSL,"SMTP")

    secure_connection("imap.gmail.com",IMAP_IMPLICIT_SSL,"IMAP")
    secure_connection("pop.gmail.com",POP_IMPLICIT_SSL,"POP")

def test_yahoo_services():
    starttls_connection("smtp.mail.yahoo.com",SMTP_STARTTLS_SSL,"SMTP")
    starttls_connection("smtp.mail.yahoo.com",SMTP_STANDARD,"SMTP")
    secure_connection("smtp.yahoo.com",SMTP_IMPLICIT_SSL,"SMTP")

    secure_connection("imap.mail.yahoo.com",IMAP_IMPLICIT_SSL,"IMAP")
    secure_connection("pop.mail.yahoo.com",POP_IMPLICIT_SSL,"POP")

def test_hotmail_services():
    starttls_connection("mx3.hotmail.com",SMTP_STANDARD,"SMTP")

def test_zoho_services():
    starttls_connection("smtp.zoho.com",SMTP_STARTTLS_SSL,"SMTP")
    secure_connection("imap.zoho.com",IMAP_IMPLICIT_SSL,"IMAP")
    secure_connection("pop.zoho.com",POP_IMPLICIT_SSL,"POP")
