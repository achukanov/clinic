from django.urls import path

from . import views

urlpatterns = [
    path('booking', views.booking_doctor, name='booking_doctor'),
    path('booking/<int:id>', views.booking_date, name='booking_date'),
    path('booking/<int:id>/<slug:date>', views.booking_time, name='booking_time')
]