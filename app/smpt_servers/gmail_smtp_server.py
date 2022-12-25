import logging
import smtplib
from email.mime.multipart import MIMEMultipart

log = logging.getLogger("send_on_mail")


class SmtpServer:

    def __init__(self, host, port, my_email, my_email_password):
        self.server = smtplib.SMTP_SSL(host, port)
        self.my_email = my_email
        self.my_email_password = my_email_password

    def start(self):
        # self.server.starttls()
        self.server.login(self.my_email, self.my_email_password)

    def close(self):
        self.server.quit()


class GmailSend(SmtpServer):

    def __init__(self, host, port, my_email, my_email_password):
        super().__init__(host, port, my_email, my_email_password)

    def send_email(self, mail: str, msg: MIMEMultipart) -> bool:
        try:

            self.server.sendmail(self.my_email, mail, msg.as_string())

            log.info('Successfully sent email')
            return True
        except Exception as e:
            log.exception(f'Error sending on email: {e}')
            return False
