from django.urls import path
from .views import *


urlpatterns = [
    path('', home),
    path('workspaces/', workspace_list),
    path('workspaces/add/', add_workspace),
    path('workspaces/update/', update_workspace),
    path('workspaces/remove/', remove_workspace),
    
    path('workspaces/<slug:slug>', task_list),
    path('workspaces/<slug:slug>/add', add_task),
    path('workspaces/<slug:slug>/update', update_task),
    path('workspaces/<slug:slug>/remove', remove_task),
    
    path('signup/', signup),
    path('login/', login),
    
]