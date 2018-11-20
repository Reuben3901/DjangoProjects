from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
# Class views
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Individual user Posts
from django.contrib.auth.models import User

def home(request):
    context={'posts' : Post.objects.all()}
    #return HttpResponse('<h1>Blog Home - Latest Posts</h1>')
    return render(request, 'blog/home.html', context, {'title':'Blog'})

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 6

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    # Ordering is overridden by the query
    #ordering = ['-date_posted']
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        # Overriding form_valid to insert author id before form valid is run
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        # Overriding form_valid to insert author id before form valid is run
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Olny allow post Author to edit post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/blog/class/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def homepage(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
