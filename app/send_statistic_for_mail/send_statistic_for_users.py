from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from app import config
from app.smpt_servers import server_smtp_gmail


def send_statistic_for_users():
    list_users = config.list_users_for_send_statistics

    # Send verification code to email
    msg, code = msg_preparation(list_users)
    server_smtp_gmail.send_email(list_users, msg)


def msg_preparation(mail: list) -> MIMEMultipart:
    # TODO Дописать вывод нужно информации

    msg = MIMEMultipart('alternative')

    msg['From'] = config.my_email
    msg['To'] = mail
    msg['Subject'] = 'Confirm your email'
    msg['Content-Type'] = 'text/html; charset=utf-8'

    msg.attach(MIMEText("<b>Verification code: " +  "</b>", 'html'))
    return msg



