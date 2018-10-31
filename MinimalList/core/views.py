from django.shortcuts import render
# from django.http import HttpResponse
from core.models import Tasks


def index(request):
    tasks = Tasks.objects.all()

    return render(request, 'index.html', {
        'tasks': tasks,
    })
