from django.shortcuts import render
from .models import Doctors
from django.http import HttpResponse


# TODO: request, title, description, phone(+7(988)8604300), phone_title(+7(988)860-43-00),
# TODO: mail(andros-008@mail.ru)
# TODO: booking(https://booking.medflex.ru/?user=d2264a28a42691145544d9fea59cf0c9)

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    doctors = Doctors.objects.all()
    return render(request,
                  'clinic/index.html', {
                      'request': request,
                      'doctors': doctors,
                      'description': "Предлагаем Вам качественное медицинское лечение и обследование по низким ценам в Ессентуках. Наш телефон: +7(988)860-43-00",
                      'phone': '+7(988)8604300',
                      'phone_title': '+7(988)860-43-00',
                      'mail': 'andros-008@mail.ru',
                      'booking': 'https://booking.medflex.ru/?user=d2264a28a42691145544d9fea59cf0c9',
                      'date': '2023'
                  })


def contacts(request):
    return render(request,
                  'clinic/contacts.html', {
                      'request': request,
                      'description': "Предлагаем Вам качественное медицинское лечение и обследование по низким ценам в Ессентуках. Наш телефон: +7(988)860-43-00",
                      'adress': 'Ставропольский край, Ессентуки г., ул. Разумовского, 7',
                      'phone': '+7(988)8604300',
                      'phone_title': '+7(988)860-43-00',
                      'mail': 'andros-008@mail.ru',
                      'date': '2023'
                  })


def about(request):
    return render(request,
                  'clinic/about.html', {
                      'request': request,
                      'description': "Предлагаем Вам качественное медицинское лечение и обследование по низким ценам в Ессентуках. Наш телефон: +7(988)860-43-00",
                      'adress': 'Ставропольский край, Ессентуки г., ул. Разумовского, 7',
                      'phone': '+7(988)8604300',
                      'phone_title': '+7(988)860-43-00',
                      'mail': 'andros-008@mail.ru',
                      'date': '2023'
                  })