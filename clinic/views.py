from django.shortcuts import render, redirect
from .models import Doctors, Specializations, Price, Certificates, Questions, Videos, Diseases
from custom.models import IndexSlider
from custom.models import Maps
from .forms import QuestionForm
from booking.models import Booking


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
    map_link = Maps.objects.filter(active=True).first()
    return render(request,
                  'clinic/contacts.html', {
                      'request': request,
                      'map_link': map_link.title
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


def laborators(request):
    return render(request, 'clinic/laborators.html')


def branch(request, slug):
    # if request.method == 'POST':
    #     form = QuestionForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('medicine')

    spec = Specializations.objects.filter(slug=slug).first()
    doctors = Doctors.objects.filter(specialization=spec).filter(active=True)
    certificates = Certificates.objects.filter(doctor__in=doctors, active=True).order_by('-sorting')
    prices = Price.objects.filter(specialization=spec, active=True).order_by('-sorting')
    diseases = Diseases.objects.filter(specialization=spec, active=True).order_by('-sorting')
    videos = Videos.objects.filter(specialization=spec, active=True).order_by('-sorting')
    # questions = Questions.objects.filter(is_answered=True, active=True).order_by('-created_at')
    form = QuestionForm(initial={'specialization': spec})
    return render(request,
                  'clinic/branch.html', {
                      'request': request,
                      'spec': spec,
                      'doctors': doctors,
                      'certificates': certificates,
                      'prices': prices,
                      'diseases': diseases,
                      'videos': videos,
                      # 'questions': questions,
                      'form': form
                  })


def doctor(request, slug, id):
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

