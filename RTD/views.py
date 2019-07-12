from django.shortcuts import render

# Create your views here.
# FUNCTII care iau cererea user ului si raspund la cerere

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>app  home page</h1>")