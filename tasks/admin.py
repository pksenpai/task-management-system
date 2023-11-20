from django.contrib import admin
from .models import User, Workspace, Task


@admin.register(User)
class UserAdmin(admin.ModelAdmin): ...

@admin.register(Workspace)
class WorkspaceAdmin(admin.ModelAdmin): ...

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin): ...
