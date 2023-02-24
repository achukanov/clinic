import datetime
from django import forms
from django.shortcuts import render, redirect
from .models import Booking
from clinic.models import Doctors, Specializations
from .forms import BookingForm
from django.utils.text import slugify


# TODO: объединить обе системы букинга через ИФ

def booking(request):

    if request.method == 'POST':
        form = BookingForm(request.POST)
        # form.fields['doctor'] = doctor
        # print(form.fields)
        # print(form.data)
        # print(form.data['time'])
        # print(type(form.data['time']))
        # for field in form:
        #     print("Field Error:", field.name, field.errors)
        # print(form.data)
        # for i in form.fields:
        #     print(i.value)
        if form.is_valid():
            dict_email = request.POST.dict()
            # print('---------------------------------------------------valid!')
            form.save()
            # send_email(dict_email=dict_email)
            # print('---------------------------------------------------save!')
            return redirect('/')
        else:
            # messages.error(request, 'Ошибка регистрации')
            return render(request, 'booking/booking.html', {"form": form})

    # now = datetime.datetime.now().time()
    # bookings = Booking.objects.filter(doctor=doctor.pk, date__gte=now).order_by('date')
    # bookings_list = []
    # for i in bookings:
    #     bookings_list.append(slugify(i.date))
    # if doctor_id:
    #     doctors = Doctors.objects.filter(active=True, pk=doctor_id).first()
    # else:
    doctors = Doctors.objects.filter(active=True).all()
    specs = Specializations.objects.filter(active=True).all()

    form = BookingForm()
    # form.fields['doctor'] = forms.ModelChoiceField(queryset=doctors.objects.all(), widget=forms.ChoiceField)
    # form.fields['spec'] = forms.ModelChoiceField(queryset=specs.objects.all(), widget=forms.ChoiceField)

    return render(request,
                  'booking/booking.html', {
                      'request': request,
                      'form': form,
                      # 'doctor': doctor,
                      # 'date': date,
                      # 'bookings': bookings,
                      # 'today': today,
                      # 'now': now
                  })
