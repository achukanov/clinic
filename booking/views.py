import datetime
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Booking
from clinic.models import Doctors, Specializations
from .forms import BookingForm
from django.utils.text import slugify
from django.core.exceptions import ValidationError

from .send_message import send_email


# TODO: редирект обратно
# TODO: логирование


def booking(request):
    if request.method == 'POST':
        next = request.POST.get('next', '/')
        form = BookingForm(request.POST)
        if form.is_valid():
            print('---------------------------------------------------valid!')
            form_data = form.save()
            doctor = form_data.doctor
            name = form_data.name
            phone = form_data.phone
            send_email(doctor=doctor, name=name, phone=phone)
            return redirect('/')
        else:
            print('---------------------------------------------------not valid!')
            print(form.fields['doctor'])
            print(form.errors)
            print('form', form.data)
            return HttpResponseRedirect(next)
            # return render(request,
            #               'booking/booking.html', {
            #                   'request': request,
            #                   'form': form
            #               })

    form = BookingForm()
    return render(request,
                  'booking/booking.html', {
                      'request': request,
                      'form': form
                  })