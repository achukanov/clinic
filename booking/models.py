from django.db import models
from clinic.models import Doctors, Specializations, Branch


'''
port = 465  # For SSL
    smtp_server = "smtp.rambler.ru"
    sender_email = "drus206@rambler.ru"  # Enter your address
    receiver_email = "a.chukanov@rambler.ru"  # Enter receiver address
    password = '2picitaliaparis'
'''


class EmailBotSettings(models.Model):
    port = models.CharField(max_length=200, verbose_name='Порт')
    smtp_server = models.CharField(max_length=200, verbose_name='smtp сервер')
    sender_email = models.TextField(max_length=200, verbose_name='Почта отправления')
    password = models.TextField(max_length=200, verbose_name='Пароль почты отправления')
    receiver_email = models.TextField(max_length=200, verbose_name='Почта получателя')

    def __str__(self):
        return self.smtp_server

    class Meta:
        verbose_name = 'Настройки почтового бота'
        verbose_name_plural = 'Настройки почтового бота'


class Booking(models.Model):
    # spec = models.ForeignKey(Specializations, on_delete=models.RESTRICT, verbose_name='Специализация', blank=False)
    doctor = models.ForeignKey(Doctors, on_delete=models.RESTRICT, verbose_name='Врач', blank=False)
    name = models.CharField(max_length=200, verbose_name='Имя', blank=False)
    phone = models.CharField(max_length=50, verbose_name='Номер телефона', blank=False)
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявку'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_at']
