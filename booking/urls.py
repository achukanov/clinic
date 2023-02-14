from django.urls import path

from . import views

urlpatterns = [
    path('booking', views.booking, name='booking'),
    path('booking/<int:id>', views.booking_doctor, name='booking_doctor')
]