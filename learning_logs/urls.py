'''Defines URL patterns for learning_logs.'''

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name = 'home'),
    path('topics/',views.topics, name = 'topics'),
    path()
]