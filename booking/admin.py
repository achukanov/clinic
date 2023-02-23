from django.contrib import admin

from .models import Booking, Times, BookingRequests


class BookingAdmin(admin.ModelAdmin):
    list_display = ('date', 'doctor', 'context')
    list_display_links = ('date', 'doctor', 'context')
    list_filter = ('date', 'doctor')
    search_fields = ('date', 'context',)


class TimesAdmin(admin.ModelAdmin):
    list_display = ('time',)
    list_display_links = ('time',)
    ordering = ('time',)


class BookingRequestsAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'doctor', 'branch', 'initials', 'birthdate', 'phone')


admin.site.register(Booking, BookingAdmin)
admin.site.register(Times, TimesAdmin)
admin.site.register(BookingRequests, BookingRequestsAdmin)

admin.site.site_title = 'Бронь'
admin.site.site_header = 'Бронь'
