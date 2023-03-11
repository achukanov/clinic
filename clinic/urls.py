from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    # path('', cache_page(60*15)(views.index), name='index'),
    path('', views.index, name='index'),
    path('contacts', cache_page(60*150)(views.contacts), name='contacts'),
    # path('about', cache_page(60*150)(views.about), name='about'),
    path('medicine', cache_page(60*15)(views.medicine), name='medicine'),
    # path('medicine/<slug:slug>', cache_page(60*15)(views.branch), name='branch'),
    path('medicine/<slug:slug>', views.branch, name='branch'),
    # path('doctors/<int:id>', cache_page(60*15)(views.doctor), name='doctor'),
    path('doctors/<int:id>', views.doctor, name='doctor'),
    path('prices', cache_page(60*15)(views.price), name='price'),
    path('laborators', cache_page(60*150)(views.laboratories), name='laborators'),
]
