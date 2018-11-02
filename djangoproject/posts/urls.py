from django.conf.urls import url
from . import views

url:patterns = [
    url('', views.index, name='index'),
    url('details/(?P<id>\d+)', views.details, name='details')
    ]
