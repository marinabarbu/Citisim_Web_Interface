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

energy_set = set()
def select(request):
    all_energy = Energy.objects.all()
    #energy_set = set()
    for e in all_energy:
        energy_set.add(e.time_string[0:10])
    energy_time = list(energy_set)
    return render(request, 'RTD/select.html', {'energy_time': energy_time})

def action_action(request):
    if request.GET.get('action_button'):
        l = (list(energy_set)).sort()
        print('actiune buton')
    return render(request, 'RTD/select.html', {'l': l})


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
        all_energy = Energy.objects.all()
        return render(request, 'RTD/charts.html')

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = User.objects.all().count()
        all_energy = Energy.objects.filter(time_string__startswith='07', source='0A06FF0000000003')
        iulie_labels, iulie_data = [], []
        for e in all_energy:
            iulie_labels.append(e.idd)
            iulie_data.append(e.data)
        all_energy = Energy.objects.filter(time_string__startswith='08', source='0A06FF0000000003')
        august_labels, august_data = [], []
        for e in all_energy:
            august_labels.append(e.idd)
            august_data.append(e.data)

        all_energy = Energy.objects.filter(time_string__startswith='09', source='0A06FF0000000003')
        septembrie_labels, septembrie_data = [], []
        for e in all_energy:
            septembrie_labels.append(e.idd)
            septembrie_data.append(e.data)
        data = {
            "labels_iulie": iulie_labels,
            "default_iulie": iulie_data,
            "labels_august": august_labels,
            "default_august": august_data,
            "labels_septembrie": septembrie_labels,
            "default_septembrie": septembrie_data,
        }
        return Response(data)
