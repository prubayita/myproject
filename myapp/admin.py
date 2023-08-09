from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'startDate', 'endDate', 'assignee', 'project', 'priority']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name']
