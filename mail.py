import os
import smtplib
from email.header import Header
from email.mime.text import MIMEText


class Mail:
    debug_level = True if os.getenv('FLASK_DEBUG', 0) == 1 else False

    def __init__(self, smtp=smtplib.SMTP()):
        self.from_address = None
        self.to_address = None
        self.subject = None
        self.message = None
        self.smtp = smtp

    def __enter__(self):
        return self

    def valid(self):
        if (self.from_address is None or
                self.to_address is None or
                self.to_address is None or
                self.subject is None or
                self.message is None):
            return False
        return True

    def __exit__(self, exc_type, exc_value, traceback):
        if not self.valid():
            # TODO: add log 'No send mail'
            return
        msg = MIMEText(self.message)
        msg['Subject'] = Header(self.subject)
        msg['From'] = self.from_address
        msg['To'] = self.to_address

        self.smtp.sendmail(self.from_address, self.to_address, msg.as_string())
        self.smtp.close()
