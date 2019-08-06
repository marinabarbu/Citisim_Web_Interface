from django.conf.urls import url, include
from . import  views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<e_idd>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<e_source>[a-z0-9A-Z]+)/$', views.data_source, name='data_source'),
    url(r'^data/$', views.get_data, name='get_data')
]