from django import forms
from .models import Booking
from clinic.models import *
import re
from django.core.exceptions import ValidationError


class BookingForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(BookingForm, self).__init__(*args, **kwargs)
        # spec_list = Specializations.objects.filter(active=True).order_by('-sorting')
        # doc_list = Doctors.objects.filter(active=True).order_by('-sorting')
        # print([i.title for i in spec_list])
        # print([i.title for i in doc_list])
        # for i in doc_list:
        #     print(i.title)
        # self.fields['spec'].queryset = spec_list
        # self.fields['doctor'].choices = doc_list

    class Meta:
        # spec_list = Specializations.objects.filter(active=True).order_by('-sorting')
        # print(spec_list)
        doc_list = Doctors.objects.filter(active=True).order_by('-sorting')
        # print('doc_list in form:', doc_list)
        # print(doc_list)
        model = Booking
        fields = ['doctor', 'name', 'phone']
        # fields = ['spec', 'doctor', 'name', 'phone']
        # spec = forms.ModelChoiceField(queryset=spec_list,
        #                               required=True)
        doctor = forms.ModelChoiceField(queryset=doc_list, required=True)

    # def clean_phone(self):
    #     phone = self.cleaned_data['phone']
    #     print('phone', phone)
    #     if not phone.isdigit():
    #         raise ValidationError('В поле могут быть только цифры')
    #     return phone

        # widgets = {
        #     'name': forms.TextInput(),
        #     'phone': forms.NumberInput(),
        # }

    # def clean_spec(self):
    #     spec = self.cleaned_data['spec']
    #     print('spec---------------------', spec)
    #     if not spec:
    #         raise ValidationError('выберите поле')
    #     return spec

    # def clean_doctor(self):
    #     doctor = self.cleaned_data['doctor']
    #     print('doctor---------------------', doctor)
    #     if not doctor:
    #         raise ValidationError('')
    #     return doctor

    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #     print('name', name)
    #     if re.match(r'\d', name):
    #         raise ValidationError('В поле не может быть цифр')
    #     return name
    #
    # def clean_phone(self):
    #     phone = self.cleaned_data['phone']
    #     print('phone', phone)
    #     if re.match(r'\w', phone):
    #         raise ValidationError('В поле не может быть букв')
    #     return phone

        #     'time': forms.ChoiceField(attrs={'name': 'time'}),
        #     'doctor': forms.HiddenInput(attrs={'name': 'doctor'}),
        #     'branch': forms.ChoiceField(attrs={'name': 'branch'}),
        #     'initials': forms.CharField(attrs={'placeholder': 'ФИО', 'name': 'initials'}),
        #     'birthdate': forms.CharField(attrs={'placeholder': 'Дата рождения', 'name': 'birthdate'}),
        #     'phone': forms.CharField(attrs={'placeholder': 'Телефон', 'name': 'phone'})
        # }
        # widgets = {
        # 'date': forms.HiddenInput(attrs={'name': 'date'}),
        # 'time': forms.ChoiceField(attrs={'name': 'time'}),
        # 'doctor': forms.HiddenInput(attrs={'name': 'doctor'}),
        # 'branch': forms.ChoiceField(attrs={'name': 'branch'}),
        # 'initials': forms.CharField(attrs={'placeholder': 'ФИО', 'name': 'initials'}),
        # 'birthdate': forms.CharField(attrs={'placeholder': 'Дата рождения', 'name': 'birthdate'}),
        # 'phone': forms.CharField(attrs={'placeholder': 'Телефон', 'name': 'phone'})
        # }
