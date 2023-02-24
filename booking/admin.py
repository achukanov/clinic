from django.contrib import admin

from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    list_display = ('spec', 'doctor', 'name', 'phone')
    list_display_links = ('name', 'phone')
    list_filter = ('spec', 'doctor')
    search_fields = ('spec', 'doctor',)
    # readonly_fields = ('created_at',)


admin.site.register(Booking, BookingAdmin)

admin.site.site_title = 'Заявки'
admin.site.site_header = 'Заявки'
