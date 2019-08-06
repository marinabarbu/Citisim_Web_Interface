from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Energy
from django.http import JsonResponse
from django.template import loader

# Create your views here.
# FUNCTII care iau cererea user ului si raspund la cerere

def index(request):
    all_energy = Energy.objects.all()
    return render(request, 'RTD/index.html', {'all_energy' : all_energy})

def detail(request, e_idd):
    #return HttpResponse("<h2>Details from Album id: " + str(e_id) + "</h2>")
    try:
        e = Energy.objects.all().get(idd=e_idd)
    except Energy.DoesNotExist:
        raise Http404("Nu exista aceasta data")
    return render(request, 'RTD/detail.html', {'e': e})


def data_source(request, e_source):
    all_energy = Energy.objects.filter(source=e_source)
    return render(request, 'RTD/data_source.html', {'all_energy' : all_energy})

def get_data(request):
    all_energy = Energy.objects.all()
    return render(request, 'RTD/get_data.html', {'all_energy' : all_energy})



