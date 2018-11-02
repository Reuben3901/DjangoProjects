from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse('<h1>Homepage</h1>')

def home(request):
    return HttpResponse('<h1>Blog Home</h1>')

def about(request):
    return HttpResponse('<h1>Blog About</h1>')
