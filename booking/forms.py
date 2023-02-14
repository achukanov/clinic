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


class BookingRequestForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'time', 'doctor', 'spec', 'initials', 'birthdate', 'phone']
        widgets = {
            'date': forms.HiddenInput(attrs={'name': 'date'}),
            'time': forms.HiddenInput(attrs={'name': 'time'}),
            'doctor': forms.HiddenInput(attrs={'name': 'doctor'}),
            'spec': forms.ChoiceField(attrs={'placeholder': 'Специализация', 'name': 'spec'}),
            'initials': forms.TextInput(attrs={'placeholder': 'ФИО', 'name': 'initials'}),
            'birthdate': forms.CharField(attrs={'placeholder': 'Дата рождения', 'name': 'birthdate'}),
            'phone': forms.CharField(attrs={'placeholder': 'Телефон', 'name': 'phone'})
        }