from django.shortcuts import render, redirect
from .models import Doctors, Specializations, Price, Certificates, Questions
from custom.models import IndexSlider
from custom.models import Maps
from django.http import HttpResponse, HttpResponseRedirect
from .forms import QuestionForm

# TODO: request, title, description, phone(+7(988)8604300), phone_title(+7(988)860-43-00),
# TODO: mail(andros-008@mail.ru)
# TODO: booking(https://booking.medflex.ru/?user=d2264a28a42691145544d9fea59cf0c9)


def index(request):
    doctors = Doctors.objects.order_by('-sorting')
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
    specs = Specializations.objects.all()
    return render(request,
                  'clinic/medicine.html', {
                      'request': request,
                      'specs': specs
                  })


def price(request):
    prices = Price.objects.all()
    specs = Specializations.objects.all()
    return render(request,
                  'clinic/prices.html', {
                      'request': request,
                      'specs': specs,
                      'prices': prices
                  })


def laborators(request):
    return render(request, 'clinic/laborators.html')


def branch(request, slug):
    form = QuestionForm()
    spec = Specializations.objects.filter(slug=slug).first()
    doctors = Doctors.objects.filter(specialization=spec)
    certificates = Certificates.objects.filter(doctor__in=doctors)
    print(spec.id)
    return render(request,
                  'clinic/branch.html', {
                      'request': request,
                      'spec': spec.id,
                      'doctors': doctors,
                      'certificates': certificates,
                      'form': form
                  })


def add_question(request):
    if request.method == 'POST':
        spec_obj = request.POST['specialization']
        # spec_obj = Specializations.objects.filter(title=spec).first()
        name = request.POST['name']
        print(name, 'name----------------', type(name))
        print(spec_obj, 'spec_obj----------------', type(spec_obj))
        # print(spec, 'spec----------------', type(spec))

        text = request.POST['text']
        form = QuestionForm(initial={'name': name, 'text': text, 'specialization': spec_obj})
        print(form.data, form.fields)
        print('---------------------')
        # form.name = request.POST['name']
        # form.text = request.POST['text']
        # form.specialization = spec_obj
        # print(form.data, form.fields)
        # spec = form.fields['specialization']
        # print(spec, 'spec-=---')
        # print(form.data)
        if form.is_valid():
            print('valid --------------------------------------')
            print(form)
            # question = Questions.objects.create(**form.cleaned_data)
            question = form.save()
            return redirect(medicine)
        else:
            print('not valid-------------------------------')
            question = form.save()
            return redirect(medicine)
    #     form = QuestionForm()
    # return render(request.META.get('HTTP_REFERER'), {'form': form})
