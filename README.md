# SSL-MAIL-PROTOCOLS-TESTING

A python Script to test SSL configurations on Mail Servers

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





