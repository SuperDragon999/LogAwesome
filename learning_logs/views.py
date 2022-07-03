from django.shortcuts import render
from .models import Topic

def index(request):
    return render(request, 'learning_logs/home.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)