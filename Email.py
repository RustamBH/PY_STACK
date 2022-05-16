import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

GMAIL_SMTP = "smtp.gmail.com"
GMAIL_IMAP = "imap.gmail.com"


class Email:
    def __init__(self, _from_addr, _password):
        self._from_addr = _from_addr
        self._password = _password

    def send(self, _recipients, _subject, _message):
        msg = MIMEMultipart()
        msg['From'] = self._from_addr
        msg['To'] = ', '.join(_recipients)
        msg['Subject'] = _subject
        msg.attach(MIMEText(_message))

        ms = smtplib.SMTP(GMAIL_SMTP, 587)
        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()

        ms.login(self._from_addr, self._password)
        ms.sendmail(self._from_addr, _recipients, msg.as_string())

    def recieve(self, header=None):
        mail = imaplib.IMAP4_SSL(GMAIL_IMAP)
        mail.login(self._from_addr, self._password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()


if __name__ == '__main__':
    from_addr = 'login@gmail.com'
    password = 'qwerty'
    subject = 'Subject'
    recipients = ['vasya@email.com', 'petya@email.com']
    message = 'Message'

    mail = Email(from_addr, password)
    mail.send(recipients, subject, message)
    mail.recieve()
