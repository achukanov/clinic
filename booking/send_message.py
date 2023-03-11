import smtplib, ssl
import socket
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from booking.models import EmailBotSettings
import logging


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
        try:
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, msg.as_string())
                logging.info(f'Письмо с бронированием отправлено на почту {receiver_email}')
        except socket.gaierror as err:
            logging.critical(f'Неверно заданы параметры почтового бота! {err}')
        except smtplib.SMTPServerDisconnected as err:
            logging.critical(f'Нет соединения с SMTPServer почтового бота! {err}')
    else:
        logging.critical(f'Не заданы параметры почтового бота!')
