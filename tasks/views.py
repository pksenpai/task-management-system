from django.shortcuts import render, HttpResponse
from .models import *


"""\_________________________MAIN_________________________/"""

def home(request):
    template = "home.html"
    return render(request, template)

"""\______________________WORKSPACE______________________/"""

def workspace_list(request):
    public_workspaces = Workspace.objects.filter(public=True)
    context = {
        'pws': public_workspaces
    }
    template = 'workspace_list.html'
    return render(request, template, context=context)
    
def add_workspace(request): ...
def update_workspace(request): ...
def remove_workspace(request): ...
def workspace_member_count(request): ...

"""\________________________TASK________________________/"""

def task_list(request): ...
def add_task(request): ...
def update_task(request): ...
def remove_task(request): ...

"""\________________________USER________________________/"""

def signup(request): ...
def login(request): ...

