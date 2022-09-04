'''Defines URL patterns for users'''
from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    # Include default auth urls
    path('',include('django.contrib.auth.urls')),
    #Registration
    path('register/', views.register, name = 'register'),
    #Redirected login
    path('redirected_login/', views.redirected_login, name = 'redirected_login'),
]