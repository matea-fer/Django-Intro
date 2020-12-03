from django import forms
from tasks import models


class TaskForm(forms.Form):
    title = forms.CharField(label='Title', max_length=160)
    description = forms.CharField(
        label='Description', widget=forms.Textarea, required=False)
    deadline = forms.DateTimeField(label='Deadline', required=False)
    priority = forms.ChoiceField(
        label="Priority", choices=models.Task.PRIORITY_CHOICES, required=False)


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ['title', 'description', 'deadline', 'priority']

