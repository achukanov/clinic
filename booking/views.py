import datetime
from django import forms
from django.shortcuts import render, redirect
from .models import Booking
from clinic.models import Doctors
from .forms import BookingForm
from django.utils.text import slugify


# TODO: объединить обе системы букинга через ИФ
def booking_doctor(request):
    doctors = Doctors.objects.filter(active=True)

    now = datetime.date.today()
    # doctor = Doctors.objects.filter(active=True, pk=id).first()
    bookings = Booking.objects.filter(date__gte=now).order_by('date')
    today = datetime.date.today()
    now = datetime.datetime.now().time()

    bookings_list = {}
    for doctor in doctors:
        doc = []
        for booking in bookings:
            if booking.doctor == doctor:
                doc.append(booking)
        bookings_list[doctor] = doc

    print(bookings_list)

    # bookings_list = []
    # for i in bookings:
    #     bookings_list.append(slugify(i.date))

    return render(request,
                  'booking/booking_doctor.html', {
                      'request': request,
                      'doctors': doctors,

                      'bookings': bookings_list,
                      'today': today,
                      'now': now

                  })


# TODO: добавление в лог после бронирования успешно/неуспешно
# TODO: повторная проверка перед записью в базу
# TODO: фильтр доступного времени перенести с шаблона во вьюху
def booking_date(request, id):
    now = datetime.date.today()
    doctor = Doctors.objects.filter(active=True, pk=id).first()
    bookings = Booking.objects.filter(doctor=doctor.pk, date__gte=now).order_by('date')
    today = datetime.date.today()
    now = datetime.datetime.now().time()

    bookings_list = []
    for i in bookings:
        bookings_list.append(slugify(i.date))
    # form = ChoiceForm()
    # queryset = doctor.branch
    # form.fields['date'] = forms.ModelChoiceField(queryset=bookings, widget=forms.RadioSelect)
    # form.fields['branch'] = forms.ModelChoiceField(queryset=queryset, widget=forms.RadioSelect)
    return render(request,
                  'booking/booking_date.html', {
                      'request': request,
                      'doctor': doctor,
                      'bookings': bookings_list,
                      'today': today,
                      # 'form': form,
                      'now': now
                  })


def booking_time(request, id, date):
    doctor = Doctors.objects.filter(active=True, pk=id).first()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        # form.fields['doctor'] = doctor
        print(form.fields)
        print(form.data)
        print(form.data['time'])
        print(type(form.data['time']))
        for field in form:
            print("Field Error:", field.name, field.errors)
        # print(form.data)
        # for i in form.fields:
        #     print(i.value)

        if form.is_valid():

            print('---------------------------------------------------valid!')
            form.save()
            print('---------------------------------------------------save!')
            return redirect('/')

    # now = datetime.datetime.now().time()
    # bookings = Booking.objects.filter(doctor=doctor.pk, date__gte=now).order_by('date')
    # bookings_list = []
    # for i in bookings:
    #     bookings_list.append(slugify(i.date))

    date_from_slug = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    booking = Booking.objects.filter(doctor=doctor.pk, date=date_from_slug).first()
    branches = Booking.objects.filter(doctor=doctor.pk, date=date_from_slug).first()

    times = []
    for time in booking.time.all():
        times.append(time.time)
    print(times)
    form = BookingForm(initial={'doctor': doctor, 'date': date})
    # TODO:вывод в варианты выбора формы time а не str
    form.fields['time'] = forms.ModelChoiceField(queryset=booking.time.all().order_by('time'), widget=forms.RadioSelect)
    # form.fields['time'] = forms.ModelChoiceField(queryset=times, widget=forms.RadioSelect)
    form.fields['branch'] = forms.ModelChoiceField(queryset=doctor.branch.all(), widget=forms.RadioSelect)

    return render(request,
                  'booking/booking_time.html', {
                      'request': request,
                      'form': form,
                      'doctor': doctor,
                      'date': date,
                      # 'bookings': bookings,
                      # 'today': today,
                      # 'now': now
                  })
