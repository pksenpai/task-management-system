from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from .forms import AddNewTaskForm
from .models import Task
from workspaces.models import Workspace


"""\________________________TASK________________________/"""
@login_required
def all_tasks(request, id):
    searched = request.GET.get('searched')
    style = {
        'pb': 'pb-4',
        'mb': 'mb-4',
    }
    if searched:
        searched_tasks = Task.objects.filter( 
            title__icontains=searched
        ).order_by('-status')
        context = {
            'style': style,
            'WsId': id,
            'tasks': searched_tasks,
        }
        
    else:    
        tasks = Task.objects.filter(workspace__id=id).order_by('-status')
        context = {
            'style': style,
            'WsId': id,
            'tasks': tasks,
        }
    template = 'task_list.html'
    return render(request, template, context=context)

@login_required
def done_tasks(request, id):
    searched = request.GET.get('searched')
    style = {
        'pb': 'pb-4',
        'mb': 'mb-4',
    }
    tasks = Task.objects.filter(
        Q(workspace__id=id) & 
        Q(status=True)
    )
    if searched:
        searched_tasks = tasks.filter( 
            title__icontains=searched
        )
        context = {
            'style': style,
            'WsId': id,
            'tasks': searched_tasks,
        }
        
    else:    
        context = {
            'style': style,
            'WsId': id,
            'tasks': tasks,
        }
    
    template = 'task_list.html'
    return render(request, template, context=context)

@login_required
def pending_tasks(request, id):
    searched = request.GET.get('searched')
    tasks = Task.objects.filter(
        Q(workspace__id=id) & 
        Q(status=False)
    )
    style = {
        'pb': 'pb-4',
        'mb': 'mb-4',
    } 
    
    if searched:
        searched_tasks = tasks.filter( 
            title__icontains=searched
        )
        context = {
            'style': style,
            'WsId': id,
            'tasks': searched_tasks,
        }
        
    else:    
        context = {
            'style': style,
            'WsId': id,
            'tasks': tasks,
        }
    template = 'task_list.html'
    return render(request, template, context=context)

@login_required
def own_tasks(request, id):
    searched = request.GET.get('searched')
    tasks = Task.objects.filter(
        Q(workspace__id=id) & 
        Q(status=False)
    )
    style = {
        'bottom': 'border-bottom-0',
    }
    form = AddNewTaskForm()
    if request.method == 'POST':
        form = AddNewTaskForm(request.POST or None)
        if form.is_valid():
            
            task_data = form.save(commit=False)
            task_data.workspace = Workspace.objects.get(id=id)
            form.save()
            
            messages.success(
                request, 
                f'your Task created Successfully! :D'
            )
            return redirect(reverse('tasks:mytasks', args=[id]))
        
    if searched:
        searched_tasks = tasks.filter( 
            title__icontains=searched
        )
        context = {
            'style': style,
            'WsId': id,
            'tasks': searched_tasks,
            'form': form,
        }
        
    else:    
        context = {
            'style': style,
            'WsId': id,
            'tasks': tasks,
            'form': form,
        }

    template = 'task_list.html'
    return render(request, template, context=context)


