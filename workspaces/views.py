from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q, F
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import *
from .models import *


"""\__________________________WORKSPACE__________________________/"""

"""\______________________ALL______________________/"""
def all_workspace_list(request):
    searched = request.GET.get('searched')
    if searched:
        searched.strip()

    style = {
        'pb': 'pb-4',
        'mb': 'mb-4',
    }
    if searched:
        searched_workspaces = Workspace.objects.select_related('category').filter(
            Q(public=True), 
            Q(name__icontains=searched) | 
            Q(tag__title__icontains=searched) | 
            Q(category__title__icontains=searched)
        ).distinct().order_by('-member_count')
        context = {
            'style': style,
            'pws': searched_workspaces
        }
    
    else:    
        all_public_workspaces = Workspace.objects.prefetch_related('members').filter(public=True).order_by('-member_count')
        context = {
            'style': style,
            'pws': all_public_workspaces,
        }
    
    template = 'workspace_list.html'
    return render(request, template, context=context)

"""\______________________JOINED______________________/"""
@login_required
def joined_workspace_list(request):
    searched = request.GET.get('searched')
    if searched:
        searched.strip()
    
    style = {
        'pb': 'pb-4',
        'mb': 'mb-4',
    }
    if searched:
        searched_workspaces = Workspace.objects.select_related('category').filter(
            Q(public=True), 
            Q(name__icontains=searched) | 
            Q(tag__title__icontains=searched) | 
            Q(category__title__icontains=searched)
        ).distinct().order_by('-member_count')
        context = {
            'style': style,
            'pws': searched_workspaces
        }
    
    else:
        joined_workspaces = Workspace.objects.prefetch_related('members').all().order_by('-member_count')
        
        context = {
            'style': style,
            'pws': joined_workspaces,
        }
        
    template = 'workspace_list.html'
    return render(request, template, context=context)

"""\______________________OWN______________________/"""
@login_required
def own_workspace_list(request):
    searched = request.GET.get('searched')
    if searched:
        searched.strip()
    
    style = {
        'pb': 'pb-4',
        'mb': 'mb-4',
    }
    if searched:
        searched_workspaces = Workspace.objects.select_related('category').filter(
            Q(public=True), 
            Q(name__icontains=searched) | 
            Q(tag__title__icontains=searched) | 
            Q(category__title__icontains=searched)
        ).distinct().order_by('-member_count')
        context = {
            'style': style,
            'pws': searched_workspaces
        }

    if request.method == "POST":
        form = AddNewWorkspaceForm(request.POST or None)
        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.host = request.user
            
            form.save()
            messages.success(
                request, 
                f'your Workspace created Successfully! :D'
            )
            return redirect(reverse('workspaces:own'))
    
    style = {
        'bottom': 'border-bottom-0',
    }
    own_workspaces = Workspace.objects.select_related('category').filter(host=request.user).order_by('-member_count')
    form = AddNewWorkspaceForm() # Add new ws Form
    context = {
        'style': style,
        'pws': own_workspaces,
        'form': form,
    }
    template = 'workspace_list.html'
    return render(request, template, context=context)

def Workspace_details(request, id):
    workspace_detail = Workspace.objects.get(id=id)
    tags             = Tag.objects.prefetch_related('workspace').filter(workspace__id=id)

    if request.method == 'POST': # BUG FIX THIS...<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        form = JoinMemberForm()
        form.members = request.user
        
        number_of_members = Workspace.objects.get(id=id).member_count
        print(number_of_members)
        form.member_count = number_of_members + 1
        
        form.save()
        
        messages.success(
            request, 
            f'Welcome to {workspace_detail.name} '
        )
        return redirect(reverse('tasks:all', args=[id]))
        
    context = {
        'footer': True,
        'WsId': id,
        'tags': tags,
        'wsd': workspace_detail,
    }
    
    template = 'workspace_details.html'
    return render(request, template, context=context)
    
@login_required
def Workspace_update(request, id):
    workspace = Workspace.objects.get(id=id)
    form = UpdateWorkspaceForm(instance=workspace)
    if request.method == "POST":
        form = UpdateWorkspaceForm(request.POST, instance=workspace)
        print('================', request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(
                request, 
                f'your Workspace update Successfully! :D'
            )
            return redirect(reverse('workspaces:own'))
    
    context = {
        'footer': True,
        'form': form,
        'ws': workspace
    }
    template = 'update_workspace.html'
    return render(request, template, context=context)

@login_required
def Workspace_delete(request, id):
    workspace = Workspace.objects.get(
        Q(id=id) & 
        Q(host=request.user) | 
        Q(edit_ws_permission=request.user)
    )
    workspace.delete()
    return redirect(reverse('workspaces:own'))
    
