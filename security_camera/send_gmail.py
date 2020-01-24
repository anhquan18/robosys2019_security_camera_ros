import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.utils import formatdate

FROM_ADDRESS = 'quanz1812@gmail.com'
MY_PASSWORD = 'Bomemay1812'
TO_ADDRESS = 'quan181219@gmail.com'
BCC = ''
SUBJECT = 'GmailのSMTPサーバ経由'
CONTENT = 'pythonでメール送信'


def create_message(from_addr, to_addr, bcc_addrs, subject, content):
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Bcc'] = bcc_addrs
    msg['Date'] = formatdate()
    return msg


def create_msg_with_image(from_addr, to_addr, bcc_addrs, subject, content):
    # Read file as binary
    with open("ononoki.jpeg",'rb') as img_file: # can also do with file(filename, 'rb')
        img_data = img_file.read()
    print("img type:", type(img_data))
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr

    text = MIMEText(content)
    msg.attach(text)
    image = MIMEImage(img_data, _subtype="jpeg")#, name=os.path.basename('./ononoki.jpeg'))
    msg.attach(image)

    return msg


def send(from_addr, to_addrs, msg):
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.ehlo()
    smtpobj.login(FROM_ADDRESS, MY_PASSWORD)
    smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
    smtpobj.close()


if __name__ == '__main__':

    to_addr = TO_ADDRESS
    subject = SUBJECT

    #msg = create_message(FROM_ADDRESS, to_addr, BCC, subject, CONTENT)
    msg = create_msg_with_image(FROM_ADDRESS, to_addr, BCC, subject, CONTENT)
    send(FROM_ADDRESS, to_addr, msg)
