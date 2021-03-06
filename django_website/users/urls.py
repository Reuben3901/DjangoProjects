from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='users-home'),
    path('biography/', views.biography, name='users-biography'),
    path('settings/', views.settings, name='users-settings'),
    path('profile/', views.profile, name='users-profile'),
    path('portfolio/', views.portfolio, name='users-portfolio'),
    path('register/', views.register, name='users-register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='users-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='users-logout'),
    path('password-reset/',
        auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
            name='password_reset'),
    path('password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
            name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>',
        auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
            name='password_reset_confirm'),
    path('password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
            name='password_reset_complete'),



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


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
