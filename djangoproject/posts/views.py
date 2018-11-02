from django.shortcuts import render
from .models import Posts
# Create your views here.
def index(request):
    posts = Posts.objects.all()[:10]
    #you could have Posts.all here and posts.all in the loop
    context = {
        'title' : 'Latest Posts',
        'posts' : posts
        }
    #return render(request, 'posts/index.html', {'title': 'Latest Posts'})
    return render(request, 'posts/index.html', context)

def details(request,id):
    post = Posts.objects.get(id=id)
    context = {
        'post' : post
        }
    return render(request, 'posts/details.html', context)

