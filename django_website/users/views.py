from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Post
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm

#Import our new custom form from forms.py
# for def register
#import django default user creation form
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import ProfilePictures

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
    context = { 'pics' : ProfilePictures.objects.all() }
    return render(request, 'users/portfolio.html', context, {'title':'Portfolio'})

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
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
            instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('users-profile')
            
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request,'users/profile.html', context)
