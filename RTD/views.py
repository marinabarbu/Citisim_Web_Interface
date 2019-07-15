from django.shortcuts import render
from django.http import Http404
from .models import Energy
from django.template import loader

# Create your views here.
# FUNCTII care iau cererea user ului si raspund la cerere

def index(request):
    all_energy = Energy.objects.all()
    return render(request, 'RTD/index.html', {'all_energy' : all_energy})

def detail(request, e_id):
    try:
        e = Energy.objects.get(pk=e_id)
    except Energy.DoesNotExist:
        raise Http404("Nu exista aceasta data")
    return render(request, 'RTD/detail.html', {'e': e})
