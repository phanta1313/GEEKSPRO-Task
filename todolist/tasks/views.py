from django.shortcuts import render
from .forms import *
from .models import *
def showTasks(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'index.html', context)
def showTask(request,pk):
    task = Task.objects.get(pk=pk)

    context = {'task': task}
    return render(request, 'index.html', context)
def createTask(request):
    task = Task()
    if request.method == "POST":
        task = Task()
        f
    context = {'task': task}
    return render(request, 'index.html', context)
def editTask(request):
    
    task = Task()
    if request.method == "PUT":
        task = Task()

    context = {'task': task}
    return render(request, 'index.html', context)
def deleteTask(request):
    task = Task()
    if request.method == "DELETE":
        task = Task()

    context = {'task': task}
    return render(request, 'index.html', context)