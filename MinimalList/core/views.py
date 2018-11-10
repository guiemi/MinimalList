from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Tasks, Projects
from datetime import datetime


def index(request):
    tasks = Tasks.objects.all()
    projects = Projects.objects.all()
    today_date = datetime.now()

    if request.method == 'POST':
        if "taskAdd" in request.POST:
            taskAdd = request.POST["taskAdd"]
            Todo = Tasks(taskAdd=taskAdd)
            Todo.save()
            return redirect('/')

        if "projectAdd" in request.POST:
            projectAdd = request.POST["projectAdd"]
            Project = Projects(projectAdd=projectAdd)
            Project.save()
            return redirect('/')

    elif request.method == 'GET':
        return render(request, 'index.html', {
            'tasks': tasks,
            'projects': projects,
            'today_date': today_date,

        })
