from django.db import models
from django.utils.html import mark_safe
from clinic.models import Specializations


class Maps(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', blank=True)
    title = models.TextField(verbose_name='HTML код карты для вставки в сайт', blank=False)
    active = models.BooleanField(default=False, verbose_name='Активно (ТОЛЬКО ОДНА АКТИВНА!)')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Карту'
        verbose_name_plural = 'Карты'
        ordering = ['-active']


class IndexSlider(models.Model):
    photo = models.ImageField(upload_to='index_slider/', verbose_name='Изображение')
    sorting = models.IntegerField(default=0, verbose_name='Приоритет')
    active = models.BooleanField(default=True, verbose_name='Активно')

    def image_tag(self):
        if self.photo:
            return mark_safe(f'<img src="{self.photo.url}" width="150px" height="150px" />')
        else:
            return ''

    image_tag.short_description = 'Фото'

    class Meta:
        verbose_name = 'Слайдер главной страницы'
        verbose_name_plural = 'Слайдер главной страницы'
        ordering = ['sorting']


class OtherData(models.Model):
    number = models.IntegerField(verbose_name='Номер ячейки', blank=True)
    title = models.TextField(verbose_name='Описание')
    data = models.CharField(max_length=240, verbose_name='Информация', blank=True)

    class Meta:
        verbose_name = 'Информацию для сайта'
        verbose_name_plural = 'Информация для сайта'
