from django.contrib import admin
from django.urls import path
from authapp.views import UserRegistrationView
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("auth/", views.auth, name="auth"),
    #path("stats/", views.stats, name="stats"),
    path('register/', UserRegistrationView.as_view(), name='register_user'),
    path('login/', views.user_login, name='user_login'),  # Corrected path
    path('logout/', views.user_logout, name='logout'),  # Corrected path
    path('google-login/', views.google_login, name='google_login'),
    path('totp-login/', views.totp_login, name='totp_login'),
    #path('user-login/', views.user_login, name='login'),
    path("dashboard/", views.dashboard, name="dashboard"),
    path('register_totp/', views.register_totp, name='register_totp'),
]
