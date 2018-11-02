from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post

def index(request):
    context={'posts' : Post.objects.all()}
    return render(request, 'users/index.html', context, {'title':'Index'})


def biography(request):
    return render(request, 'users/biography.html', {'title':'Biography'})

def settings(request):
    return render(request, 'users/settings.html', {'title':'Settings'})

def portfolio(request):
    #return HttpResponse('<h1>Blog Home - Latest Posts</h1>')
    return render(request, 'users/portfolio.html', {'title':'Portfolio'})

#import django default user creation form
from django.contrib.auth.forms import UserCreationForm
def register(request):
    form = UserCreationForm()
    return render(request,'users/register.html',{'form':form})
