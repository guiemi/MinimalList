from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Tasks
from datetime import datetime


def index(request):
    tasks = Tasks.objects.all()
    today_date = datetime.now()

    if request.method == 'POST':
        if "taskAdd" in request.POST:
            taskAdd = request.POST["taskAdd"]
            Todo = Tasks(taskAdd=taskAdd)
            Todo.save()
            return redirect('/')
    elif request.method == 'GET':
        return render(request, 'index.html', {
            'tasks': tasks,
            'today_date': today_date,
        })
