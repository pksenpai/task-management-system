from django.urls import path
from .views import *


app_name = 'workspaces'
urlpatterns = [
    path('all/', all_workspace_list, name='all'),
    path('joined/', joined_workspace_list, name='joined'),
    path('own/', own_workspace_list, name='own'),
]

