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


# def new_task(request):
#     add_task = Tasks(task_name = request.POST['new_task'])
#     add_task.save()
#     return HttpResponseRedirect('/')
