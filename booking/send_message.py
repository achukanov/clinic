import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

from booking.models import EmailBotSettings

'настройки отправки почты'
EMAIL_PORT = 465  # For SSL
SMTP_SERVER = "smtp.rambler.ru"
SENDER_EMAIL = "drus206@rambler.ru"  # Enter your address
RECEIVER_EMAIL = "a.chukanov@rambler.ru"  # Enter receiver address
EMAIL_PASSWORD = '2picitaliaparis'


def send_email(doctor, name, phone):
    parameters = EmailBotSettings.objects.first()
    print('---------------------------------------------------in sendemail')
    port = parameters.port  # For SSL
    smtp_server = parameters.smtp_server
    sender_email = parameters.sender_email  # Enter your address
    receiver_email = parameters.receiver_email  # Enter receiver address
    password = parameters.password
    # message = """\
    # Subject: Hi there
    #
    # This message is sent from Python."""
    message = f'ЗАЯВКА С САЙТА ' \
              f'Доктор: {doctor},' \
              f'Имя: {name},' \
              f'Телефон: {phone}'
    msg = MIMEText(message, _charset="UTF-8")
    msg = MIMEMultipart('alternative')
    msg['Subject'] = Header('Заголовок', "utf-8")

    msg = MIMEMultipart()
    msg['Subject'] = "Заголовок"
    msg['From'] = sender_email
    msg['To'] = receiver_email
    text = f'ЗАЯВКА С САЙТА ' \
                  f'Доктор: {doctor},' \
                  f'Имя: {name},' \
                  f'Телефон: {phone}'
    msg.attach(MIMEText(text, 'plain'))

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        # server.sendmail(sender_email, receiver_email, message.encode("utf8"))
        server.sendmail(sender_email, receiver_email, msg.as_string())
