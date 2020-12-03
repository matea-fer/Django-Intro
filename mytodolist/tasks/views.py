from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.utils.timezone import now
from tasks.models import Task
from django.shortcuts import get_object_or_404
from tasks.forms import TaskForm, TaskModelForm

class TaskListView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'tasks': Task.objects.all()
        }
        return render(request, 'tasks/task_list.html', context=context)


class  TaskDetailsView(View):
    def get(self, request, task_id):
        #try:
        #    context = {
        #        'task': Task.objects.get(id=task_id)
        #    }
        #except Task.DoesNotExist:
        #    return  HttpResponse('Task not found', status=404)
        context = {
               'task': get_object_or_404(Task, id=task_id)
           }
        return render(request, 'tasks/task_details.html', context=context)


class TaskEditView(View):

    def get(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        form = TaskModelForm(instance=task)
        context = {
            'task': task,
            'form': form
        }
        return render(request, 'tasks/task_edit.html', context=context)

    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        form = TaskModelForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('task_list'))
        context = {'task': task, 'form': form}
        return render(request, 'tasks/task_edit.html', context=context)

    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        form = TaskForm(request.POST)
        if form.is_valid():
            task.title = form.cleaned_data['title']
            task.description = form.cleaned_data['description']
            task.deadline = form.cleaned_data['deadline']
            task.priority = form.cleaned_data['priority']
            task.save()
            return HttpResponseRedirect(reverse('task_list'))
        context = {'task': task, 'form': form}
        return render(request, 'tasks/task_edit.html', context=context)


class  TaskDeleteView(View):
    def get(self, request, task_id):
        #Task.objects.get(id=task_id).delete()
        context = {
            'task':Task.objects.get(id=task_id)
        }
        return render(request, 'tasks/task_delete.html', context=context)

    def post(self, request, task_id):
        Task.objects.get(id=task_id).delete()
        return HttpResponseRedirect(reverse('task_list'))

class TaskCreateView(View):
    def get(self, request):
        form = TaskModelForm()
        context = {
            'form': form
        }
        return render(request, 'tasks/task_create.html', context=context)

    def post(self, request):
        form = TaskModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('task_list'))
        context = {'form': form}
        return  render(request, 'tasks/task_create.html', context=context)