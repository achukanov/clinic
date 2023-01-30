from django.shortcuts import render, redirect
from .models import Doctors, Specializations, Price, Certificates, Questions
from custom.models import Maps
from django.http import HttpResponse, HttpResponseRedirect
from .forms import QuestionForm

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
    map_link = Maps.objects.filter(active=True).first()
    return render(request,
                  'clinic/contacts.html', {
                      'request': request,
                      'map_link': map_link.title,
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


def medicine(request):
    specs = Specializations.objects.all()
    return render(request,
                  'clinic/medicine.html', {
                      'request': request,
                      'specs': specs,
                      'description': "Предлагаем Вам качественное медицинское лечение и обследование по низким ценам в Ессентуках. Наш телефон: +7(988)860-43-00",
                      'adress': 'Ставропольский край, Ессентуки г., ул. Разумовского, 7',
                      'phone': '+7(988)8604300',
                      'phone_title': '+7(988)860-43-00',
                      'mail': 'andros-008@mail.ru',
                      'date': '2023'
                  })


def price(request):
    prices = Price.objects.all()
    specs = Specializations.objects.all()
    return render(request,
                  'clinic/prices.html', {
                      'request': request,
                      'specs': specs,
                      'prices': prices,
                      'description': "Предлагаем Вам качественное медицинское лечение и обследование по низким ценам в Ессентуках. Наш телефон: +7(988)860-43-00",
                      'adress': 'Ставропольский край, Ессентуки г., ул. Разумовского, 7',
                      'phone': '+7(988)8604300',
                      'phone_title': '+7(988)860-43-00',
                      'mail': 'andros-008@mail.ru',
                      'date': '2023'
                  })


def laborators(request):
    return render(request, 'clinic/laborators.html')


def branch(request, slug):
    form = QuestionForm()
    spec = Specializations.objects.filter(slug=slug).first()
    doctors = Doctors.objects.filter(specialization=spec)
    certificates = Certificates.objects.filter(doctor__in=doctors)
    return render(request,
                  'clinic/branch.html', {
                      'request': request,
                      'spec': spec,
                      'doctors': doctors,
                      'certificates': certificates,
                      'form': form
                  })


def add_question(request):
    if request.method == 'POST':
        spec = request.POST['specialization']
        spec_obj = Specializations.objects.filter(title=spec).first()
        name = request.POST['name']
        print(name, 'name----------------', type(name))
        print(spec_obj, 'spec_obj----------------', type(spec_obj), spec_obj.title)
        print(spec, 'spec----------------', type(spec))

        text = request.POST['text']
        form = QuestionForm(initial={'name': name, 'text': text, 'specialization': spec_obj})
        print(form.data, form.fields)
        print('---------------------')
        # form.name = request.POST['name']
        # form.text = request.POST['text']
        # form.specialization = spec_obj
        # print(form.data, form.fields)
        # spec = form.fields['specialization']
        # print(spec, 'spec-=---')
        # print(form.data)
        if form.is_valid():
            print('valid --------------------------------------')
            print(form)
            # question = Questions.objects.create(**form.cleaned_data)
            question = form.save()
            return redirect(medicine)
        else:
            print('not valid-------------------------------')
            question = form.save()
            return redirect(medicine)
    #     form = QuestionForm()
    # return render(request.META.get('HTTP_REFERER'), {'form': form})
