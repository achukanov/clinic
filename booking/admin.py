from django.contrib import admin

from .models import Booking, Times


class BookingAdmin(admin.ModelAdmin):
    list_display = ('date', 'doctor', 'context')
    list_display_links = ('date', 'doctor', 'context')
    list_filter = ('date', 'doctor')
    search_fields = ('date', 'context',)


class TimesAdmin(admin.ModelAdmin):
    list_display = ('time',)
    list_display_links = ('time',)
    ordering = ('time',)


admin.site.register(Booking, BookingAdmin)
admin.site.register(Times, TimesAdmin)

admin.site.site_title = 'Бронь'
admin.site.site_header = 'Бронь'