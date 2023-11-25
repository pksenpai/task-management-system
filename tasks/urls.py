from django.urls import path
from .views import *


app_name = 'tasks'
urlpatterns = [
    path('<int:id>/', task_list, name='task_list'),
    path('<int:id>/add/', add_task, name='add_task'),
    path('<int:id>/update/', update_task, name='update_task'),
    path('<int:id>/remove/', remove_task, name='remove_task'),
]

