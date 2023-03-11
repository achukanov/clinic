from django.shortcuts import render
from .models import Doctors, Specializations, Price, Certificates, Videos, Diseases, SpecSlider
from custom.models import IndexSlider
from custom.models import Maps


def index(request):
    doctors = Doctors.objects.filter(active=True).order_by('-sorting')
    slider = IndexSlider.objects.filter(active=True).order_by('-sorting')
    return render(request,
                  'clinic/index.html', {
                      'request': request,
                      'doctors': doctors,
                      'slider': slider
                  })


def contacts(request):
    map = Maps.objects.filter(active=True).first()
    map_link = map.title if map else ' '
    return render(request,
                  'clinic/contacts.html', {
                      'request': request,
                      'map_link': map_link
                  })


def about(request):
    return render(request,
                  'clinic/about.html', {
                      'request': request
                  })


def medicine(request):
    specs = Specializations.objects.filter(active=True)
    return render(request,
                  'clinic/medicine.html', {
                      'request': request,
                      'specs': specs
                  })


def price(request):
    prices = Price.objects.filter(active=True).order_by('-sorting')
    specs = Specializations.objects.filter(active=True)
    return render(request,
                  'clinic/prices.html', {
                      'request': request,
                      'specs': specs,
                      'prices': prices
                  })


def laboratories(request):
    return render(request, 'clinic/laboratories.html')


def branch(request, slug):
    spec = Specializations.objects.filter(slug=slug).first()
    doctors = Doctors.objects.filter(specialization=spec).filter(active=True)
    certificates = Certificates.objects.filter(doctor__in=doctors, active=True).order_by('-sorting')
    prices = Price.objects.filter(specialization=spec, active=True).order_by('-sorting')
    diseases = Diseases.objects.filter(specialization=spec, active=True).order_by('-sorting')
    videos = Videos.objects.filter(specialization=spec, active=True).order_by('-sorting')
    slider = SpecSlider.objects.filter(specialization=spec, active=True).order_by('-sorting')
    return render(request,
                  'clinic/branch.html', {
                      'request': request,
                      'spec': spec,
                      'doctors': doctors,
                      'certificates': certificates,
                      'prices': prices,
                      'diseases': diseases,
                      'videos': videos,
                      'slider': slider
                  })


def doctor(request, id):
    doc = Doctors.objects.filter(pk=int(id), active=True).first()
    videos = Videos.objects.filter(doctor=doc, active=True).order_by('-sorting')
    certificates = Certificates.objects.filter(doctor=doc, active=True).order_by('-sorting')
    return render(request,
                  'clinic/doctor.html', {
                      'request': request,
                      'doctor': doc,
                      'videos': videos,
                      'certificates': certificates
                  })


def probe(request):
    print('request', request)
    print('after request')
    return render(request, 'clinic/probe.html')

