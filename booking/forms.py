from django import forms
from .models import Booking
from clinic.models import *


class BookingForm(forms.ModelForm):
    class Meta:
        doc_list = Doctors.objects.filter(active=True).order_by('-sorting')
        model = Booking
        fields = ['doctor', 'name', 'phone']
        doctor = forms.ModelChoiceField(queryset=doc_list, required=True)
