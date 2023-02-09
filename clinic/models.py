from django.db import models
from autoslug import AutoSlugField
from django.utils.html import mark_safe
from os.path import splitext
from uuid import uuid4
from django.core.files.storage import FileSystemStorage


class UUIDFileStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        _, ext = splitext(name)
        return uuid4().hex + ext


class Specializations(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    slug = AutoSlugField(populate_from='title', unique=True, verbose_name='SLUG', db_index=True)
    sorting = models.IntegerField(default=0, verbose_name='Приоритет')
    active = models.BooleanField(default=True, verbose_name='Активно')
    text = models.TextField(verbose_name='Текст', blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Специализацию'
        verbose_name_plural = 'Специализации'
        ordering = ['-sorting']


class Doctors(models.Model):
    title = models.CharField(max_length=50, verbose_name='ФИО')
    description = models.TextField(verbose_name='Дополнение', blank=True)
    education = models.TextField(verbose_name='Направление', blank=True)
    education_full = models.TextField(verbose_name='Образование', blank=True)
    sorting = models.IntegerField(default=0, verbose_name='Приоритет')
    active = models.BooleanField(default=True, verbose_name='Активно')
    photo = models.ImageField(upload_to='photos/', verbose_name='Фото', blank=True, storage=UUIDFileStorage())
    link = models.URLField(blank=True)

    specialization = models.ManyToManyField(Specializations, verbose_name='Специальность', blank=True,
                                            related_name='Врачи')

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.photo:
            return mark_safe('<img src="%s" width="100px" height="100px" />' % self.photo.url)

    image_tag.short_description = 'Фото'

    class Meta:
        verbose_name = 'Врача'
        verbose_name_plural = 'Врачи'
        ordering = ['-sorting']


class Certificates(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название', blank=True)
    photo = models.ImageField(upload_to='certificates/', verbose_name='Фото', blank=False, storage=UUIDFileStorage())
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    active = models.BooleanField(default=True, verbose_name='Активно')
    sorting = models.IntegerField(default=0, verbose_name='Приоритет')

    doctor = models.ForeignKey(Doctors, on_delete=models.RESTRICT, verbose_name='Доктор')

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.photo:
            return mark_safe(f'<img src="{self.photo.url}" width="100px" height="100px" />')
        else:
            return ''

    image_tag.short_description = 'Фото'

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'
        ordering = ['created_at']


class Articles(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Заголовок', blank=False)
    slug = AutoSlugField(populate_from='title', unique=True, verbose_name='SLUG')
    text = models.TextField(verbose_name='Текст', blank=False)
    photo = models.ImageField(upload_to='articles/', verbose_name='Изображение', blank=True, storage=UUIDFileStorage())
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    active = models.BooleanField(default=True, verbose_name='Активно')

    specialization = models.ForeignKey(Specializations, on_delete=models.RESTRICT, verbose_name='Специальность')

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.photo:
            return mark_safe(f'<img src="{self.photo.url}" width="100px" height="100px" />')
        else:
            return ''

    image_tag.short_description = 'Фото'

    class Meta:
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'
        ordering = ['updated_at']


class Questions(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя', blank=False)
    text = models.TextField(verbose_name='Вопрос', blank=False)
    answer = models.TextField(verbose_name='Ответ', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления', blank=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', blank=True)
    active = models.BooleanField(default=True, verbose_name='Активен', blank=True)
    is_answered = models.BooleanField(default=False, verbose_name='Есть ответ', blank=True)

    specialization = models.ForeignKey(Specializations, on_delete=models.RESTRICT, verbose_name='Специальность')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['created_at']


class Price(models.Model):
    name = models.CharField(max_length=50, verbose_name='Услуга')
    cost = models.IntegerField(default=0, verbose_name='Цена')
    sorting = models.IntegerField(default=0, verbose_name='Приоритет')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    active = models.BooleanField(default=True, verbose_name='Активно')

    specialization = models.ManyToManyField(Specializations, verbose_name='Специальность')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Прайс'
        verbose_name_plural = 'Прайс'
        ordering = ['sorting']


class Diseases(models.Model):
    title = models.CharField(max_length=100, verbose_name='Болезнь')
    slug = AutoSlugField(populate_from='title', unique=True, verbose_name='SLUG')
    text = models.TextField(verbose_name='Описание', blank=False)
    sorting = models.IntegerField(default=0, verbose_name='Приоритет')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    active = models.BooleanField(default=True, verbose_name='Активно')

    specialization = models.ForeignKey(Specializations, on_delete=models.RESTRICT, verbose_name='Специальность')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Болезнь'
        verbose_name_plural = 'Болезни'
        ordering = ['sorting']


class Videos(models.Model):
    title = models.CharField(max_length=100, blank=True, verbose_name='Название видео')
    link = models.TextField(verbose_name='Код видео youtube', blank=False)
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата добавления')
    active = models.BooleanField(default=True, verbose_name='Активно')
    sorting = models.IntegerField(default=0, verbose_name='Приоритет')

    specialization = models.ForeignKey(Specializations, on_delete=models.RESTRICT, verbose_name='Специальность')
    disease = models.ForeignKey(Diseases, on_delete=models.RESTRICT, verbose_name='Болезнь')
    doctor = models.ForeignKey(Doctors, on_delete=models.RESTRICT, verbose_name='Доктор')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
        ordering = ['created_at']