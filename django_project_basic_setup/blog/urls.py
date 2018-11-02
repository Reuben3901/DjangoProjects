from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    # this leads to blog/about
    #  No need to enter this into main URLs.PY beacause that points to the main blog url
    path('about/', views.about, name='blog-about'),
]
