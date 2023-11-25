from django.urls import path
from .views import *


app_name = 'workspaces'
urlpatterns = [
    path('', workspace_list, name='workspace_list'),
    path('add/', add_workspace, name='add_workspace'),
    path('update/', update_workspace, name='update_workspace'),
    path('remove/', remove_workspace, name='remove_workspace'),
]

