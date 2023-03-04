from django.contrib import admin

from .models import Booking, EmailBotSettings


class BookingAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'name', 'phone')
    list_display_links = ('name', 'phone')
    list_filter = ('doctor',)
    search_fields = ('doctor',)
    readonly_fields = ('created_at',)


class EmailBotSettingsAdmin(admin.ModelAdmin):
    list_display = ('smtp_server', 'sender_email', 'receiver_email')
    list_display_links = ('smtp_server',)


admin.site.register(Booking, BookingAdmin)
admin.site.register(EmailBotSettings, EmailBotSettingsAdmin)

admin.site.site_title = 'Заявки'
