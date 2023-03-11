import datetime
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Booking
from clinic.models import Doctors, Specializations
from .forms import BookingForm
from django.utils.text import slugify
from django.core.exceptions import ValidationError
import logging

from .send_message import send_email


# TODO: редирект обратно
# TODO: логирование

log = logging.getLogger('file')


def booking(request):
    if request.method == 'POST':
        next = request.POST.get('next', '/')
        form = BookingForm(request.POST)
        if form.is_valid():
            form_data = form.save()
            doctor = form_data.doctor
            name = form_data.name
            phone = form_data.phone
            logging.info(f'форма прошла валидацию: doctor - {doctor}, name - {name}, phone - {phone}')
            send_email(doctor=doctor, name=name, phone=phone)
            return HttpResponseRedirect(next)
        else:
            logging.critical(f'форма не прошла валидацию!: form - {form.data}')

    else:
        redirect('/')
