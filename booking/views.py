import datetime

from django.shortcuts import render
from .models import Booking
from clinic.models import Doctors
from .forms import BookingForm


# TODO: объединить обе системы букинга через ИФ
def booking(request):
    doctors = Doctors.objects.filter(active=True)
    # form = BookingForm()
    return render(request,
                  'booking/booking.html', {
                      'request': request,
                      'doctors': doctors
                  })


# TODO: добавление в лог после бронирования успешно/неуспешно
# TODO: повторная проверка перед записью в базу
def booking_doctor(request, id):
    now = datetime.date.today()
    doctor = Doctors.objects.filter(active=True, pk=id).first()
    bookings = Booking.objects.filter(doctor=doctor.pk, date__gte=now).order_by('date')
    today = datetime.date.today()
    now = datetime.datetime.now().time()
    return render(request,
                  'booking/booking_doctors.html', {
                      'request': request,
                      'doctor': doctor,
                      'bookings': bookings,
                      'today': today,
                      'now': now
                  })
