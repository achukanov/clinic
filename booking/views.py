import datetime
from django import forms
from django.shortcuts import render, redirect
from .models import Booking
from clinic.models import Doctors, Specializations
from .forms import BookingForm
from django.utils.text import slugify
from django.core.exceptions import ValidationError

# TODO: объединить обе системы букинга через ИФ
# TODO: редирект обратно


def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            print('---------------------------------------------------valid!')
            form.save()
            # send_email(dict_email=dict_email)
            # print('---------------------------------------------------save!')
            return redirect('/')
        else:
            print(form.errors)
            # messages.error(request, 'Ошибка регистрации')
            return render(request, 'booking/booking.html', {"form": form})

    form = BookingForm()
    return render(request,
                  'booking/booking.html', {
                      'request': request,
                      'form': form
                  })
