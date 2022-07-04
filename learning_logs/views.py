from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm

def home(request):
    '''Home page'''
    return render(request, 'learning_logs/home.html')

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    '''Adds new topic'''
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.post)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
    context = {'form':form}