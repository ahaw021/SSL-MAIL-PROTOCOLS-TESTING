# SSL-MAIL-PROTOCOLS-TESTING

A python Script to test SSL configurations on Mail Servers

Usage - the script doesn't take parameters but a couple of example are below

secure_connection("smtp.gmail.com",SMTP_IMPLICIT_SSL,"SMTP")

starttls_connection("smtp.gmail.com",SMTP_STARTTLS_SSL,"SMTP")

The aim is to assist with testing with STARTTLS troubleshooting

#Update the Credential to Valid Credentials 

EMAIL_USERNAME = b'changeme@gmail.com'
EMAIL_PASSWORD = b'changeme'

If credentials are not updated and SSL works you will get error messages. 

It's useful for troubleshooting as it show TLS/SSL transport is working. You won't be able to troubleshoot higher level protocol errors. 

