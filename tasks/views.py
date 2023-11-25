from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from .models import *


"""\________________________TASK________________________/"""
@login_required
def task_list(request, id):
    return HttpResponse(f'<h1>Hello {id}!!!</h1>')
    
def add_task(request, slug): ...
def update_task(request, slug): ...
def remove_task(request, slug): ...

