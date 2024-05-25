from django.shortcuts import render, redirect
from .forms import *
from .models import *
def showTasks(request):
    page = 'showtasks'
    tasks = Task.objects.all()
    context = {'tasks': tasks, 'page':page}
    return render(request, 'index.html', context)
def showTask(request,pk):
    page = 'showtask'
    task = Task.objects.get(pk=pk)

    context = {'task': task, 'page':page}
    return render(request, 'index.html', context)
def createTask(request):
    page = 'createtask'
    form = TaskForm(request.POST, request.FILES)

    if request.method == "POST":
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            redirect('showTasks')

    context = {'form': form, 'page':page}
    return render(request, 'index.html', context)
def editTask(request,pk):
    page = 'edittask'

    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':

        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            task = form.save()


        context = {'task': task, 'page':page}
    return render(request, 'index.html', context)
def deleteTask(request):
    page = 'deletetask'
    task = Task()
    if request.method == "DELETE":
        task = Task()

    context = {'task': task, 'page':page}
    return render(request, 'index.html', context)