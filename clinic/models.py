from django.db import models
from autoslug import AutoSlugField
from django.utils.html import mark_safe


class Specializations(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    slug = AutoSlugField(populate_from='title', unique=True, verbose_name='SLUG', db_index=True)
    sorting = models.IntegerField(default=0, verbose_name='Приоритет')
    active = models.BooleanField(default=True, verbose_name='Активно')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Специализацию'
        verbose_name_plural = 'Специализации'
        ordering = ['-sorting']


class Doctors(models.Model):
    title = models.CharField(max_length=50, verbose_name='ФИО')
    description = models.CharField(max_length=250, verbose_name='Описание', blank=True)
    education = models.CharField(max_length=250, verbose_name='Образование', blank=True)
    sorting = models.IntegerField(default=0, verbose_name='Приоритет')
    active = models.BooleanField(default=True, verbose_name='Активно')
    photo = models.ImageField(upload_to='photos/', verbose_name='Фото', blank=True)
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
    title = models.CharField(max_length=50, verbose_name='Название')
    photo = models.ImageField(upload_to='certificates/', verbose_name='Фото', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    active = models.BooleanField(default=True, verbose_name='Активно')

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
    photo = models.ImageField(upload_to='articles/', verbose_name='Изображение', blank=True)
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
    name = models.CharField(max_length=50, verbose_name='Имя')
    text = models.TextField(verbose_name='Вопрос', blank=False)
    answer = models.TextField(verbose_name='Ответ', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    old_date = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='Дата на старом сайте', blank=True)
    active = models.BooleanField(default=True, verbose_name='Активен')
    is_answered = models.BooleanField(default=False, verbose_name='Есть ответ')

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

    specialization = models.ForeignKey(Specializations, on_delete=models.RESTRICT, verbose_name='Специальность')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Прайс'
        verbose_name_plural = 'Прайс'
        ordering = ['sorting']
