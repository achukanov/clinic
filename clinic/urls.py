from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts', views.contacts, name='contacts'),
    path('about', views.about, name='about'),
    path('medicine', views.medicine, name='medicine'),
    path('medicine/<slug:slug>', views.branch, name='branch'),
    path('add-question', views.add_question, name='add-question'),
    path('prices', views.price, name='price'),
    path('laborators', views.laborators, name='laborators'),
]
