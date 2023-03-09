
import smtplib
from email.message import EmailMessage
from pathlib import Path

from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders



html_content = Path('test_mail.html').read_text()

# email = EmailMessage()
email = MIMEMultipart()

email['from'] = 'Python <darold.python@gmail.com>'
email['to'] = 'darold.trench@gmail.com'
email['subject'] = 'Good day'

# email.set_content('Aloha from Python XD, test test 1 2 3')
# email.set_content(html_content, 'html')
email.attach(MIMEText(html_content, 'html'))


filename = 'RUT96999930-7DTE52FOLIO11313253.pdf'
with open(filename, 'rb') as attachment:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f'attachment;filename={filename}')
    email.attach(part)


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login('darold.python@gmail.com', '36983698DSds')
    smtp.send_message(email)
    print('the mail was sent...')


