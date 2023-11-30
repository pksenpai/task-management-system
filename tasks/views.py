from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from .forms import *
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
        Q(workspace__id=id),
        Q(owner=request.user),
    ).order_by('due_date')
    style = {
        'bottom': 'border-bottom-0',
    }
    form = AddNewTaskForm()
    status = StatusCheckForm()
    if request.method == 'POST':
        form = AddNewTaskForm(request.POST or None)
        if form:
            if form.is_valid():
                
                form_data = form.save(commit=False)
                
                form_data.workspace_id = id
                form_data.owner_id = request.user.id
                
                form.save()
                
                messages.success(
                    request, 
                    f'your Task created Successfully! :D'
                )
                return redirect(reverse('tasks:mytasks', args=[id]))
        else:
            status = StatusCheckForm(request.POST or None)
            if status:
                if status.is_valid():
                    status.save()
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

@login_required
def task_update(request, wid, tid):
    task = Task.objects.get(Q(id=tid) & Q(owner=request.user) | Q(edit_task_permission=request.user))
    form = UpdateTaskForm(instance=task)
    if request.method == "POST":
        form = UpdateTaskForm(request.POST, instance=task)
        print('==================',form.is_valid())
        if form.is_valid():
            form.save()
            
            messages.success(
                request, 
                f'your Task updated Successfully! :D'
            )
            return redirect(reverse('tasks:mytasks', args=[wid]))
    
    context = {
        'WsId': wid,
        'task': task,
        'form': form,
    }
    template = 'update_task.html'
    return render(request, template, context=context)
    
@login_required
def task_delete(request, wid, tid):
    task = Task.objects.get(Q(id=tid) & Q(owner=request.user) | Q(edit_task_permission=request.user))
    task.delete()
    return redirect(reverse('tasks:mytasks', args=[wid]))

