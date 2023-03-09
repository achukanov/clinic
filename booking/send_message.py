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


# TODO: логирование
def send_email(doctor, name, phone):
    parameters = EmailBotSettings.objects.first()
    if parameters:
        port = parameters.port  # For SSL
        smtp_server = parameters.smtp_server  # Enter your smtp_server
        sender_email = parameters.sender_email  # Enter your address
        receiver_email = parameters.receiver_email  # Enter receiver address
        password = parameters.password

        msg = MIMEMultipart()
        msg['Subject'] = "ЗАЯВКА С САЙТА"  # Заголовок
        msg['From'] = sender_email
        msg['To'] = receiver_email
        nl = '\n'
        text = f'Доктор: {doctor} {nl}' \
               f'Имя: {name} {nl}' \
               f'Телефон: {phone}'
        msg.attach(MIMEText(text, 'plain'))

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
