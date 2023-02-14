import requests
from .models import TelegramSettings


def send_telegram(dict_tg):
    settings = TelegramSettings.objects.get(pk=1)
    token = settings.tg_token
    chat_id = settings.tg_chat
    api = 'https://api.telegram.org/bot'

    name = dict_tg.get('name')
    phone = dict_tg.get('phone')
    date = dict_tg.get('date')
    time = dict_tg.get('time')

    method = api + token + '/sendMessage'

    text = 'Заявка с сайта: \n Имя: ' + name + '\n Телефон: ' + phone + \
           '\n Дата: ' + date + '\n Время: ' + time

    req = requests.post(method, data={
        'chat_id': chat_id,
        'text': text
    })
