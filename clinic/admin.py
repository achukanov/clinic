from django.contrib import admin
from .models import *
from django.forms import TextInput, Textarea


class SpecializationsAdmin(admin.ModelAdmin):
    list_display = ('title', 'sorting', 'active')
    list_display_links = ('title', 'sorting', 'active')
    list_filter = ('sorting', 'active')
    fields = ('title', 'sorting', 'active', 'text', 'slug')
    readonly_fields = ('slug',)
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 15, 'cols': 150})},
    }


class DoctorsAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'sorting', 'active')
    list_display_links = ('image_tag', 'title', 'sorting', 'active')
    list_filter = ('sorting', 'active', 'specialization')
    search_fields = ('title', 'description', 'education')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '100'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 15, 'cols': 150})},
    }


class CertificatesAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'active', 'created_at', 'doctor', 'sorting')
    list_display_links = ('image_tag', 'title',)
    list_filter = ('active', 'doctor')
    search_fields = ('title',)
    readonly_fields = ('created_at',)


class PriceAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'sorting', 'active', 'updated_at')
    list_display_links = ('name', 'cost', 'sorting', 'active')
    list_filter = ('cost', 'sorting', 'active')
    search_fields = ('name',)
    readonly_fields = ('updated_at',)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '150'})}
    }


class DiseasesAdmin(admin.ModelAdmin):
    list_display = ('title', 'sorting', 'specialization', 'active')
    list_display_links = ('title', 'sorting', 'specialization', 'active')
    list_filter = ('specialization', 'active')
    search_fields = ('title', 'text',)
    readonly_fields = ('updated_at',)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '150'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 15, 'cols': 150})},
    }


class VideosAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'created_at', 'sorting', 'specialization', 'disease', 'doctor')
    list_display_links = ('title', 'active', 'created_at', 'sorting', 'specialization', 'disease', 'doctor')
    list_filter = ('disease', 'specialization', 'doctor', 'active')
    search_fields = ('title', 'link',)
    readonly_fields = ('created_at',)


class SpecSliderAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'sorting', 'active', 'specialization')
    list_display_links = ('image_tag', 'sorting', 'active', 'specialization')


admin.site.register(Specializations, SpecializationsAdmin)
admin.site.register(Doctors, DoctorsAdmin)
admin.site.register(Certificates, CertificatesAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Diseases, DiseasesAdmin)
admin.site.register(Videos, VideosAdmin)
admin.site.register(SpecSlider, SpecSliderAdmin)

admin.site.site_title = 'Управление сайтом'
admin.site.site_header = 'Управление сайтом'
