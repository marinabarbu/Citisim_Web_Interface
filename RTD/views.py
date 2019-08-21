from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Energy
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from django.http import JsonResponse
from django.template import loader
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model

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

class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Central", "Eastside", "Westside"]

    def get_data(self):
        """Return 3 datasets to plot."""

        return [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65]]


line_chart = TemplateView.as_view(template_name='line_chart.html')
line_chart_json = LineChartJSONView.as_view()

User = get_user_model()
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html')

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = User.objects.all().count()
        labels = ['Users', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
        default_items = [qs_count, 1234, 123, 32, 12, 2]
        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)
