'''Defines URL patterns for learning_logs.'''

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home
    path('', views.home, name = 'home'),
    # Topics
    path('topics/',views.topics, name = 'topics'),
    # Main topic page
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Topic-adding page
    path('new_topic/', views.new_topic, name = 'new_topic'),
    # Entry-adding page
    path('new_entry/<int:topic_id>/', views.new_entry, name = 'new_entry'),
    # Editing-entry page
    path('edit_entry/<int:entry_id>/', views.edit_entry, name = 'edit_entry'),
    #Delete entry/topic page
    path('delet_entry/<int:entry_id>/', views.delete_entry, name = 'delete_entry'),
    path('delet_topic/<int:topic_id>/', views.delete_topic, name = 'delete_topic'),
]