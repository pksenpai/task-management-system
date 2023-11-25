from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin): ...

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin): ...

@admin.register(Workspace)
class WorkspaceAdmin(admin.ModelAdmin): ...

