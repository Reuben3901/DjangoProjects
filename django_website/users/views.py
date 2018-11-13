from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Post
from .forms import UserRegisterForm

#Import our new custom form from forms.py
# for def register
#import django default user creation form
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request):
    context={'posts' : Post.objects.all()}
    return render(request, 'users/index.html', context, {'title':'Index'})


def biography(request):
    return render(request, 'users/biography.html', {'title':'Biography'})

@login_required
def settings(request):
    return render(request, 'users/settings.html', {'title':'Settings'})

def portfolio(request):
    #return HttpResponse('<h1>Blog Home - Latest Posts</h1>')
    return render(request, 'users/portfolio.html', {'title':'Portfolio'})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Saving the user only needs form.save()
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

#Using this with classes is a little bit different
@login_required
def profile(request):
    return render(request,'users/profile.html')
