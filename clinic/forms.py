from django import forms
from .models import Questions, Specializations


class QuestionForm(forms.ModelForm):
    name = forms.CharField()
    text = forms.CharField()
    specialization = forms.ModelChoiceField(queryset=Specializations.objects.all())

    #     queryset=Questions.objects.all(),
    #     widget=forms.MultipleHiddenInput())

    class Meta:
        model = Questions
        # fields = ['name', 'text']
        # fields = ['name', 'text', 'specialization',]
        fields = ("name", "text", "specialization",)
