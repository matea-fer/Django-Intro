from django.contrib import admin
from tasks import models

# Register your models here.

@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_filter = ['task_list', 'priority']

@admin.register(models.TaskList)
class TaskListAdmin(admin.ModelAdmin):
    pass
