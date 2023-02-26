from django.db import models
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


# TODO: created_at
class Booking(models.Model):
    spec = models.ForeignKey(Specializations, on_delete=models.RESTRICT, verbose_name='Специализация', blank=False)
    doctor = models.ForeignKey(Doctors, on_delete=models.RESTRICT, verbose_name='Врач', blank=False)
    name = models.CharField(max_length=200, verbose_name='Имя', blank=False)
    phone = models.CharField(max_length=50, verbose_name='Номер телефона', blank=False)
    # created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = 'Заявку'
        verbose_name_plural = 'Заявки'
        # ordering = ['-created_at']
