from time import strftime

from django.db import models
from clinic.models import Doctors, Specializations
from datetime import datetime


class TelegramSettings(models.Model):
    tg_token = models.CharField(max_length=200, verbose_name='Токен')
    tg_chat = models.CharField(max_length=200, verbose_name='Чат ID')
    tg_message = models.TextField(max_length=200, verbose_name='Текст сообщения')

    def __str__(self):
        return self.tg_chat

    class Meta:
        verbose_name = 'Настройки бота'
        verbose_name_plural = 'Настройки бота'


# TODO: вынести модель Times в настройки
class Times(models.Model):
    time = models.TimeField(unique=True)

    def __str__(self):
        return self.time.strftime('%H:%M')

    class Meta:
        verbose_name = 'Время для брони'
        verbose_name_plural = 'Время для брони'
        ordering = ['-time']


class Booking(models.Model):
    date = models.DateField(verbose_name='Дата', unique=False)
    doctor = models.ForeignKey(Doctors, on_delete=models.RESTRICT, verbose_name='Доктор')
    time = models.ManyToManyField(Times, verbose_name='Время')
    context = models.TextField(verbose_name='Комментарий', blank=True)

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Бронь'
        ordering = ['-date']


class BookingRequests(models.Model):
    date = models.DateField(verbose_name='Дата', blank=False)
    time = models.TimeField(verbose_name='Время', blank=False)
    doctor = models.ForeignKey(Doctors, on_delete=models.RESTRICT, verbose_name='Врач', blank=False)
    spec = models.ForeignKey(Specializations, on_delete=models.RESTRICT, verbose_name='Специальность', blank=False)
    initials = models.TextField(verbose_name='ФИО', blank=False)
    birthdate = models.CharField(max_length=50, verbose_name='Дата рождения', blank=False)
    phone = models.CharField(max_length=50, verbose_name='Номер телефона', blank=False)

    # TODO: добавить специальность для бронирования в модель врача

    # 'date': forms.HiddenInput(attrs={'name': 'date'}),
    # 'time': forms.HiddenInput(attrs={'name': 'time'}),
    # 'doctor': forms.HiddenInput(attrs={'name': 'doctor'}),
    # 'spec': forms.ChoiceField(attrs={'placeholder': 'Специализация', 'name': 'spec'}),
    # 'initials': forms.TextInput(attrs={'placeholder': 'ФИО', 'name': 'initials'}),
    # 'birthdate': forms.CharField(attrs={'placeholder': 'Дата рождения', 'name': 'birthdate'}),
    # 'phone': forms.CharField(attrs={'placeholder': 'Телефон', 'name': 'phone'})

    def __str__(self):
        return self.initials

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявка'
        ordering = ['-date', '-time']
