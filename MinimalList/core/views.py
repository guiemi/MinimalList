from django.shortcuts import render
# from django.http import HttpResponse
from .models import Tasks
from datetime import datetime

def index(request):
    tasks = Tasks.objects.all()
    today_date = datetime.now()

    return render(request, 'index.html', {
        'tasks': tasks,
        'today_date': today_date,
    })
