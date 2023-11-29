from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from .forms import *
from .models import *


"""\__________________________WORKSPACE__________________________/"""

def public_ws_query():
    return Workspace.objects.select_related('category').filter(public=True).order_by('-member_count')

"""\______________________ALL______________________/"""
def all_workspace_list(request):
    searched = request.GET.get('searched')
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
        public_workspaces = public_ws_query()
        context = {
            'style': style,
            'pws': public_workspaces,
        }
    
    template = 'workspace_list.html'
    return render(request, template, context=context)

"""\______________________JOINED______________________/"""
@login_required
def joined_workspace_list(request):
    
    style = {
        'pb': 'pb-4',
        'mb': 'mb-4',
    }
    joined_workspaces = public_ws_query()
    context = {
        'style': style,
        'pws': joined_workspaces,
    }
    template = 'workspace_list.html'
    return render(request, template, context=context)

"""\______________________OWN______________________/"""
@login_required
def own_workspace_list(request): # add host field
    if request.method == "POST":
        form = AddNewWorkspaceForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(
                request, 
                f'your Workspace created Successfully! :D'
            )
            return redirect(reverse('workspaces:own'))
    
    style = {
        'bottom': 'border-bottom-0',
    }
    public_workspaces =  public_ws_query()
    form = AddNewWorkspaceForm() # Add new ws Form
    context = {
        'style': style,
        'pws': public_workspaces,
        'form': form,
    }
    template = 'workspace_list.html'
    return render(request, template, context=context)

