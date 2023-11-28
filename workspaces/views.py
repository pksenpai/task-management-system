from django.shortcuts import render, HttpResponse
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import *


"""\__________________________WORKSPACE__________________________/"""

"""\______________________ALL______________________/"""
def all_workspace_list(request):
    searched = request.GET.get('searched')
    if searched:
        searched_workspaces = Workspace.objects.filter(
            Q(public=True), 
            Q(name__icontains=searched) | 
            Q(tag__title__icontains=searched) | 
            Q(category__title__icontains=searched)
        )
        context = {
            'pws': searched_workspaces
        }
    
    else:    
        public_workspaces = Workspace.objects.filter(public=True).order_by('-member_count')
        context = {
            'pws': public_workspaces
        }
    
    template = 'workspace_list.html'
    return render(request, template, context=context)

"""\______________________JOINED______________________/"""
@login_required
def joined_workspace_list(request):
    
    joined_workspaces = Workspace.objects.filter(members__username=True).order_by('-member_count')
    context = {
        'pws': joined_workspaces
    }
    template = 'workspace_list.html'
    return render(request, template, context=context)

"""\______________________OWN______________________/"""
@login_required
def own_workspace_list(request):
    public_workspaces = Workspace.objects.filter(public=True).order_by('-member_count') # add host field
    context = {
        'pws': public_workspaces
    }
    template = 'workspace_list.html'
    return render(request, template, context=context)

def search_workspace(request, title): ...

@login_required
def add_workspace(request): ...

@login_required
def update_workspace(request): ...

@login_required
def remove_workspace(request): ...

def workspace_member_count(request): ...

