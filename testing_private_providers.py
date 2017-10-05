from connections import *
import json

def test_custom_servers():
    insecure_connection("mail.mycompany.com",1000,"SMTP")
    starttls_connection("mail.mycompany.com",1001,"POP")
    secure_connection("mail.mycompany.com",1002,"IMAP")

def test_custom_servers_from_json(filepath):
    json_data=open(filepath).read()
    mail_servers = json.loads(json_data)
    print(mail_servers)
