from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q

from .models import *


"""\________________________TASK________________________/"""
@login_required
def all_tasks(request, id):
    searched = request.GET.get('searched')
    if searched:
        searched_tasks = Task.objects.filter( 
            title__icontains=searched
        ).order_by('-status')
        context = {
            'status_filter': "all",
            'WsId': id,
            'tasks': searched_tasks,
        }
        
    else:    
        tasks = Task.objects.filter(workspace__id=id).order_by('-status')
        context = {
            'WsId': id,
            'tasks': tasks,
        }
        
    template = 'task_list.html'
    return render(request, template, context=context)

def done_tasks(request, id):
    searched = request.GET.get('searched')
    tasks = Task.objects.filter(
        Q(workspace__id=id) & 
        Q(status=True)
    )
    
    if searched:
        searched_tasks = tasks.filter( 
            title__icontains=searched
        )
        context = {
            'status_filter': "done",
            'WsId': id,
            'tasks': searched_tasks,
        }
        
    else:    
        context = {
            'WsId': id,
            'tasks': tasks,
        }
        
    template = 'task_list.html'
    return render(request, template, context=context)

def pending_tasks(request, id):
    searched = request.GET.get('searched')
    tasks = Task.objects.filter(
        Q(workspace__id=id) & 
        Q(status=False)
    )
    
    if searched:
        searched_tasks = tasks.filter( 
            title__icontains=searched
        )
        context = {
            'status_filter': "pending",
            'WsId': id,
            'tasks': searched_tasks,
        }
        
    else:    
        context = {
            'WsId': id,
            'tasks': tasks,
        }
        
    template = 'task_list.html'
    return render(request, template, context=context)
     
def add_task(request, id): ...
def update_task(request, id): ...
def remove_task(request, id): ...

