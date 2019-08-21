from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<e_idd>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<e_source>[a-z0-9A-Z]+)/$', views.data_source, name='data_source'),
    url(r'^get_data/$', views.get_data, name='get_data'),
    url(r'^chart/$', views.HomeView.as_view(), name='chart'),
    url(r'^api/chart/data/$', views.ChartData.as_view(), name='api-data'),
]