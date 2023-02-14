from django import forms
from .models import Booking


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


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'doctor', 'time']
        widgets = {
            'date': forms.Select(attrs={'name': 'date'}),
            'doctor': forms.Select(attrs={'name': 'doctor'}),
            'time': forms.Select(attrs={'name': 'time'}),
            # 'name': forms.TextInput(attrs={'placeholder': 'Имя', 'name': 'name'}),
            # 'phone': forms.NumberInput(attrs={'placeholder': 'Телефон', 'name': 'phone'}),
        }