

# def send_statistic_for_users():
#     # Send verification code to email
#     msg, code = msg_preparation(user.email)
#     server_smtp_gmail.send_email(user.email, msg)
#
#
# def msg_preparation(mail: str) -> tuple[MIMEMultipart, str]:
#     msg = MIMEMultipart('alternative')
#
#     msg['From'] = config.my_email
#     msg['To'] = mail
#     msg['Subject'] = 'Confirm your email'
#     msg['Content-Type'] = 'text/html; charset=utf-8'
#     code = msg_code()
#
#     msg.attach(MIMEText("<b>Verification code: " + code + "</b>", 'html'))
#     return msg, code