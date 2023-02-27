from datetime import datetime

from booking.forms import BookingForm
from custom.models import OtherData

'''
    'description': "Предлагаем Вам качественное медицинское лечение и обследование по низким ценам в Ессентуках. Наш телефон: +7(988)860-43-00",
    'adress': 'Ставропольский край, Ессентуки г., ул. Разумовского, 7',
    'phone': '+7(988)8604300',
    'mail': 'andros-008@mail.ru',
    'year': datetime.now().year,
    'instagram': 'https://www.instagram.com/clinic_andros_essentuki/'
    'title': 'Андрос+',
    'booking_url' - если TRUE, то медфлекс, если пустая строка - своя форма бронирования
'''


def context_tags(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
    else:
        form = BookingForm()
    data = OtherData.objects.all().order_by('number')
    context = {
        'booking_url': data[0].data,
        'description': data[1].data,
        'title': data[2].data,
        'address': data[3].data,
        'phone': data[4].data,
        'mail': data[5].data,
        'year': datetime.now().year,
        'instagram': data[6].data,
        'form': form
    }
    return context


'''
    OtherData.objects.all()
    0 - Ссылка на бронирование
    1 - META-description страницы
    2 - title
    3 - адрес
    4 - Номер телефона
    5 - почта
    6 - Ссылка на инстаграм
'''
