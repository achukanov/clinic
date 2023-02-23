from django import forms
from .models import BookingRequests, Booking
from clinic.models import *


# class QuestionForm(forms.ModelForm):
#
#     class Meta:
#         model = Questions
#         fields = ("name", "text", "specialization")
#         widgets = {
#             'name': forms.TextInput(attrs={
#                 'class': 'uk-input uk-form-large uk-box-shadow-medium',
#                 'id': 'id_name',
#                 'placeholder': 'Имя---',
#                 'name': 'name'}),
#             'text': forms.Textarea(attrs={
#                 'class': 'uk-textarea uk-form-large uk-box-shadow-medium',
#                 'id': 'id_text',
#                 'placeholder': 'Текст---',
#                 'name': 'text',
#                 'rows': 5}),
#             'specialization': forms.HiddenInput()
#         }

# class ChoiceForm(forms.Form):
#     # doctor = Doctors.objects.filter(id=7).all()
#     # print(doctor)
#     # doctor = forms.ModelChoiceField(queryset=Doctors.objects.all(), to_field_name='title')
#     queryset = Booking.objects.all()
#     date = forms.ModelChoiceField(queryset=queryset)
#     branch = forms.ModelChoiceField(queryset=queryset)
#
#     class Meta:
#         fields = ['date', 'branch']
#         # widgets = {
#         #     'doctor': forms.HiddenInput(),
#         #     'date': forms.ChoiceField(),
#         #     'time': forms.ChoiceField()
#         # }

class BookingForm(forms.ModelForm):
    # queryset = Booking.objects.all()
    # date = forms.HiddenInput(),
    # time = forms.ModelChoiceField(queryset=queryset),
    # doctor = forms.HiddenInput(),
    # branch = forms.ModelChoiceField(queryset=queryset),
    # initials = forms.CharField(),
    # birthdate = forms.CharField(),
    # phone = forms.CharField()

    class Meta:
        model = BookingRequests
        fields = ['date', 'time', 'doctor', 'branch', 'initials', 'birthdate', 'phone']
        # widgets = {
        #     'date': forms.HiddenInput(attrs={'name': 'date'}),
        #     'time': forms.ChoiceField(attrs={'name': 'time'}),
        #     'doctor': forms.HiddenInput(attrs={'name': 'doctor'}),
        #     'branch': forms.ChoiceField(attrs={'name': 'branch'}),
        #     'initials': forms.CharField(attrs={'placeholder': 'ФИО', 'name': 'initials'}),
        #     'birthdate': forms.CharField(attrs={'placeholder': 'Дата рождения', 'name': 'birthdate'}),
        #     'phone': forms.CharField(attrs={'placeholder': 'Телефон', 'name': 'phone'})
        # }
        widgets = {
            'date': forms.HiddenInput(attrs={'name': 'date'}),
            # 'time': forms.ChoiceField(attrs={'name': 'time'}),
            'doctor': forms.HiddenInput(attrs={'name': 'doctor'}),
            # 'branch': forms.ChoiceField(attrs={'name': 'branch'}),
            # 'initials': forms.CharField(attrs={'placeholder': 'ФИО', 'name': 'initials'}),
            # 'birthdate': forms.CharField(attrs={'placeholder': 'Дата рождения', 'name': 'birthdate'}),
            # 'phone': forms.CharField(attrs={'placeholder': 'Телефон', 'name': 'phone'})
        }
