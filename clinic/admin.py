from django.contrib import admin
from .models import *


class SpecializationsAdmin(admin.ModelAdmin):
    list_display = ('title', 'sorting', 'active')
    list_display_links = ('title', 'sorting', 'active')
    list_filter = ('sorting', 'active')
    fields = ('title', 'sorting', 'active', 'text', 'slug')
    readonly_fields = ('slug',)


class BranchAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'sorting')
    list_display_links = ('title', 'slug', 'sorting')
    list_filter = ('title', 'sorting',)
    fields = ('title', 'slug', 'sorting')
    readonly_fields = ('slug',)


class DoctorsAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'education', 'description', 'sorting', 'active')
    list_display_links = ('image_tag', 'title', 'education', 'description')
    list_filter = ('sorting', 'active', 'specialization', 'branch')
    search_fields = ('title', 'description', 'education')


class CertificatesAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'active', 'created_at', 'doctor', 'sorting')
    list_display_links = ('image_tag', 'title',)
    list_filter = ('active', 'doctor')
    search_fields = ('title',)
    readonly_fields = ('created_at',)


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'slug', 'text', 'active', 'created_at', 'updated_at', 'specialization')
    list_display_links = ('title',)
    list_filter = ('active', 'specialization')
    search_fields = ('title', 'slug', 'text')
    readonly_fields = ('slug', 'created_at', 'updated_at',)


class QuestionsAdmin(admin.ModelAdmin):
    # TODO: ограничить число символов в предпросмотре
    list_display = ('name', 'text', 'answer', 'created_at', 'updated_at', 'active', 'is_answered', 'specialization')
    list_display_links = ('name', 'text', 'answer', 'created_at', 'updated_at', 'specialization', )
    list_filter = ('active', 'is_answered', 'specialization')
    search_fields = ('name', 'text', 'answer')
    readonly_fields = ('created_at', 'updated_at',)


class PriceAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'sorting', 'active', 'updated_at')
    list_display_links = ('name', 'cost', 'sorting', 'active')
    list_filter = ('cost', 'sorting', 'active')
    search_fields = ('name',)
    readonly_fields = ('updated_at',)


class DiseasesAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'sorting', 'specialization', 'active', 'updated_at')
    list_display_links = ('title', 'text', 'sorting', 'specialization', 'active')
    list_filter = ('specialization', 'active')
    search_fields = ('title', 'text',)
    readonly_fields = ('updated_at',)


class VideosAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'active', 'created_at', 'sorting', 'specialization', 'disease', 'doctor')
    list_display_links = ('title', 'link', 'active', 'created_at', 'sorting')
    list_filter = ('disease', 'specialization', 'doctor', 'active')
    search_fields = ('title', 'link',)
    readonly_fields = ('created_at',)


admin.site.register(Specializations, SpecializationsAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Doctors, DoctorsAdmin)
admin.site.register(Certificates, CertificatesAdmin)
admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Diseases, DiseasesAdmin)
admin.site.register(Videos, VideosAdmin)

admin.site.site_title = 'Управление сайтом'
admin.site.site_header = 'Управление сайтом'
