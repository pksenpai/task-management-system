from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q

from .forms import *
from .models import Task
from workspaces.models import Workspace


def date_now():
    return timezone.now().date()

"""\________________________TASK________________________/"""
@login_required
def all_tasks(request, id):
    searched = request.GET.get('searched')
    tzn = date_now()
    
    style = {
        'pb': 'pb-4',
        'mb': 'mb-4',
    }
    if searched:
        searched_tasks = Task.objects.filter( 
            title__icontains=searched
        ).order_by('-status')
        context = {
            'tzn': tzn,
            'style': style,
            'WsId': id,
            'tasks': searched_tasks,
        }
        
    else:    
        tasks = Task.objects.filter(workspace__id=id).order_by('-status')
        context = {
            'tzn': tzn,
            'style': style,
            'WsId': id,
            'tasks': tasks,
        }
    template = 'task_list.html'
    return render(request, template, context=context)

@login_required
def done_tasks(request, id):
    searched = request.GET.get('searched')
    tzn = date_now()
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
            'tzn': tzn,
            'style': style,
            'WsId': id,
            'tasks': searched_tasks,
        }
        
    else:    
        context = {
            'tzn': tzn,
            'style': style,
            'WsId': id,
            'tasks': tasks,
        }
    
    template = 'task_list.html'
    return render(request, template, context=context)

@login_required
def pending_tasks(request, id):
    searched = request.GET.get('searched')
    tzn = date_now()
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
            'tzn': tzn,
            'style': style,
            'WsId': id,
            'tasks': searched_tasks,
        }
        
    else:    
        context = {
            'tzn': tzn,
            'style': style,
            'WsId': id,
            'tasks': tasks,
        }
    template = 'task_list.html'
    return render(request, template, context=context)

@login_required
def own_tasks(request, id):
    searched = request.GET.get('searched')
    tzn = date_now()
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
            'tzn': tzn,
            'style': style,
            'WsId': id,
            'tasks': searched_tasks,
            'form': form,
        }
        
    else:    
        context = {
            'tzn': tzn,
            'style': style,
            'WsId': id,
            'tasks': tasks,
            'form': form,
        }

    template = 'task_list.html'
    return render(request, template, context=context)

@login_required
def task_update(request, wid, tid):
    task = Task.objects.select_related('workspace').get(
        Q(id=tid) &
        Q(pk=wid) &
        Q(owner=request.user) |
        Q(edit_task_permission=request.user)
    )
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
    task = Task.objects.select_related('workspace').get(
        Q(id=tid) &
        Q(pk=wid) &
        Q(owner=request.user) |
        Q(edit_task_permission=request.user)
    )
    if task:
        task.delete()
        messages.success(
            request, 
            f'Your task has been Successfully deleted!'
        )
    else:
        messages.error(
            request, 
            f'Sorry! This task has Not been deleted! :D'
        )
        
    return redirect(reverse('tasks:mytasks', args=[wid]))

@login_required
def task_complete(request, wid, tid):
    task = Task.objects.select_related('workspace').get(
        Q(id=tid) &
        Q(pk=wid) &
        Q(owner=request.user) |
        Q(functor_task_permission=request.user)
    )
    if task:
        if task.status:
            task.status = False
            messages.success(
                request,
                f'Your task has been Back to uncomplete! :('
            )
            task.save()            
            
        else:
            task.status = True
            messages.success(
                request,
                f'Congratulations! Your task has been Successfully completed! :D'
            )
            task.save()
        
    else:
        messages.error(
            request, 
            f'Sorry! This task has Not been done! :D'
        )
                
    return redirect(reverse('tasks:mytasks', args=[wid]))
    

@login_required
def atom(request):
    searched = request.GET.get('searched')
    tzn = date_now()
    
    all_tasks_of_mine = Task.objects.filter(
        Q(owner=request.user) | 
        Q(functor_task_permission=request.user)
    ).order_by('status')
    
    style = {
        'pb': 'pb-4',
        'mb': 'mb-4',
    } 
    if searched:
        searched_tasks = all_tasks_of_mine.filter( 
            title__icontains=searched
        )
        context = {
            'tzn': tzn,
            'footer': True,
            'style': style,
            'WsId': id,
            'tasks': searched_tasks,
        }
    
    else:
        context = {
            'tzn': tzn,
            'footer': True,
            'style': style,
            'WsId': id,
            'tasks': all_tasks_of_mine,
        }
        
    template = 'all_tasks_of_mine.html'
    return render(request, template, context=context)
    
