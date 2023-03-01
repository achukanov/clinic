from django.contrib import admin
from .models import *
from django.forms import TextInput, Textarea


class MapsAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')
    list_display_links = ('name', 'active')


class IndexSliderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'type', 'sorting', 'active')
    list_display_links = ('pk', 'type', 'sorting', 'active')
    # fields = ('photo', 'sorting', 'active')


class OtherDataAdmin(admin.ModelAdmin):
    list_display = ('number', 'title')
    list_display_links = ('number', 'title')
    ordering = ('number',)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '100'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 100})},
    }


admin.site.register(Maps, MapsAdmin)
admin.site.register(IndexSlider, IndexSliderAdmin)
admin.site.register(OtherData, OtherDataAdmin)


admin.site.site_title = 'Информация'
admin.site.site_header = 'Информация'