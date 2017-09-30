import connections

def gmail_services():
    starttls_connection("smtp.gmail.com",SMTP_STARTTLS_SSL,"SMTP","TLS1")
    starttls_connection("smtp.gmail.com",SMTP_STANDARD,"SMTP","TLS1")

    secure_connection("imap.gmail.com",IMAP_IMPLICIT_SSL,"IMAP","TLS1")
    secure_connection("pop.gmail.com",POP_IMPLICIT_SSL,"POP","TLS1")

def yahoo_services():
    starttls_connection("smtp.mail.yahoo.com",SMTP_STARTTLS_SSL,"SMTP","TLS1")
    starttls_connection("smtp.mail.yahoo.com",SMTP_STANDARD,"SMTP","TLS1")
    secure_connection("smtp.yahoo.com",SMTP_IMPLICIT_SSL,"SMTP","TLS1")

    secure_connection("imap.mail.yahoo.com",IMAP_IMPLICIT_SSL,"IMAP","TLS1")
    secure_connection("pop.mail.yahoo.com",POP_IMPLICIT_SSL,"POP","TLS1")

def hotmail_services():
    starttls_connection("mx3.hotmail.com",SMTP_STANDARD,"SMTP","TLS1")

def zoho_services():
    starttls_connection("smtp.zoho.com",SMTP_STARTTLS_SSL,"SMTP","TLS1")
    secure_connection("imap.zoho.com",IMAP_IMPLICIT_SSL,"IMAP","TLS1")
    secure_connection("pop.zoho.com",POP_IMPLICIT_SSL,"POP","TLS1")



#
