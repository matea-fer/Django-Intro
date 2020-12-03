from django.db import models
from django.utils import timezone
# Create your models here.

class Task(models.Model):
    PRIORITY_CHOICES = [(1, 'Low'), (3, 'Medium'), (5, 'High')]

    title = models.CharField(max_length=160)
    description = models.TextField(null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)

    priority = models.IntegerField(
        null=True, blank=True, choices=PRIORITY_CHOICES
    )

    created_at = models.DateTimeField(editable=False, default=timezone.now)

    task_list = models.ForeignKey(
        'TaskList',
        on_delete=models.CASCADE,
        #na task listi mi kreiraj object tasks, obrnuta relacija
        #postoje dvije strane relacije
        related_name='tasks',
        null=True,
        blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('created_at',)

class TaskList(models.Model):

    title = models.CharField(max_length=80, unique=True)
    def __str__(self):
        return self.title
