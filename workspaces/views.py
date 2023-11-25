from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import *


"""\______________________WORKSPACE______________________/"""

def workspace_list(request):
    public_workspaces = Workspace.objects.filter(public=True).order_by('-member_count')
    context = {
        'pws': public_workspaces
    }
    template = 'workspace_list.html'
    return render(request, template, context=context)

@login_required
def add_workspace(request): ...

@login_required
def update_workspace(request): ...

@login_required
def remove_workspace(request): ...

def workspace_member_count(request): ...

