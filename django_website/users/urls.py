from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='users-home'),
    path('biography/', views.biography, name='users-biography'),
    path('settings/', views.settings, name='users-settings'),
    path('portfolio/', views.portfolio, name='users-portfolio'),
    #path('', PostListView.as_view(), name='blog-home'),
    #path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    # this leads to blog/about
    #  No need to enter this into main URLs.PY beacause that points to the main blog url
    #path('about/', views.about, name='blog-about'),
    #path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    # Shares template with update view
    #path('post/new/', PostCreateView.as_view(), name='post-create'),
    #path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    #path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

]
