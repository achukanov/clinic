from django.contrib import admin
from .models import Maps, IndexSlider, OtherData


class MapsAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'active')
    list_display_links = ('name', 'title', 'active')
    fields = ('name', 'title', 'active')


class IndexSliderAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'sorting', 'active')
    list_display_links = ('image_tag', 'sorting', 'active')
    fields = ('photo', 'sorting', 'active')


class OtherDataAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'data')
    list_display_links = ('number', 'title', 'data')
    fields = ('number', 'title', 'data')
    ordering = ('number',)

admin.site.register(Maps, MapsAdmin)
admin.site.register(IndexSlider, IndexSliderAdmin)
admin.site.register(OtherData, OtherDataAdmin)

admin.site.site_title = 'Информация'
admin.site.site_header = 'Информация'