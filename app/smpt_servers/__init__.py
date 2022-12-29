from app import config
from app.smpt_servers.gmail_smtp_server import GmailSend

server_smtp_gmail = GmailSend(
    config.smtp_server_gmail,
    config.smtp_port_gmail,
    config.my_email,
    config.my_email_password,
)
