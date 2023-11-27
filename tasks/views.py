from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from .models import *


"""\________________________TASK________________________/"""
@login_required
def task_list(request, id):
    tasks = Task.objects.filter(workspace__id=id).order_by('-status')
    context = {
        'tasks': tasks
    }
    template = 'task_list.html'
    return render(request, template, context=context)
    
def add_task(request, slug): ...
def update_task(request, slug): ...
def remove_task(request, slug): ...

