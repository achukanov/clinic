import datetime
from django import forms
from django.shortcuts import render
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
    date_from_slug = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    booking = Booking.objects.filter(doctor=doctor.pk, date=date_from_slug).first()
    branches = Booking.objects.filter(doctor=doctor.pk, date=date_from_slug).first()
    times = []
    # for time in booking.time.all():
    #     print(time.time)
    #     times.append(time.time)
    # print(sorted(times))
    form = BookingForm()
    # print(form)
    # print('-----------------------------------------------------------------------------------------------------------')
    # print(form.fields)
    form.fields['time'] = forms.ModelChoiceField(queryset=booking.time.all().order_by('time'), widget=forms.RadioSelect)
    form.fields['branch'] = forms.ModelChoiceField(queryset=doctor.branch.all(), widget=forms.RadioSelect)
    # print(sorted(times))
    # print(form)
    # print(form.fields)
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
