import smtplib, ssl, requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

port = 465  # For SSL
smtp_server = "smtp.gmail.com"


def constructMsgObject(msgText, senderEmail, senderPassword, receiverEmail):
    msg = MIMEMultipart()
    msg['From'] = senderEmail
    msg['To'] = receiverEmail
    msg['Subject'] = "Amazon product prices as of today"
    msg.attach(MIMEText(msgText, 'plain'))
    return msg


def sendEmail(msgText, senderEmail, senderPassword, receiverEmail):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        msg = constructMsgObject(msgText, senderEmail, senderPassword, receiverEmail)
        print(msg.as_string())
        server.login(senderEmail, senderPassword)
        server.sendmail(senderEmail, receiverEmail, msg.as_string())

