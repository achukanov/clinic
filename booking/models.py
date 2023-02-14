from time import strftime

from django.db import models
from clinic.models import Doctors
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
