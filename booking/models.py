from django.db import models
from smart_selects.db_fields import ChainedForeignKey, ChainedManyToManyField
from clinic.models import Doctors, Specializations, Branch


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
    # time = models. ManyToManyField(Times, verbose_name='Время')
    time = models.ManyToManyField(Times, verbose_name='Время')
    context = models.TextField(verbose_name='Комментарий', blank=True)

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Бронь'
        ordering = ['-date']


class BookingRequests(models.Model):
    date = models.CharField(max_length=50, verbose_name='Дата', blank=False)
    time = models.CharField(max_length=50, verbose_name='Время', blank=False)
    doctor = models.ForeignKey(Doctors, on_delete=models.RESTRICT, verbose_name='Врач', blank=False)
    branch = models.ForeignKey(Branch, on_delete=models.RESTRICT, verbose_name='Специальность врача', blank=False)
    initials = models.TextField(verbose_name='ФИО', blank=False)
    birthdate = models.CharField(max_length=50, verbose_name='Дата рождения', blank=False)
    phone = models.CharField(max_length=50, verbose_name='Номер телефона', blank=False)

    def __str__(self):
        return self.initials

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявка'
        ordering = ['-date', '-time']
