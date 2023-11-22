from django.contrib import admin
from .models import User, Workspace, Task, Tag, Category


@admin.register(User)
class UserAdmin(admin.ModelAdmin): ...

@admin.register(Workspace)
class WorkspaceAdmin(admin.ModelAdmin): ...

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin): ...

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin): ...

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin): ...
