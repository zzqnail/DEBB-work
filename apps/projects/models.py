from django.db import models
from django.contrib.auth.models import User

from apps.team.models import Team


# Create your models here.

class Project(models.Model):
    STATUS_CHOICES = [
        ('новая', 'Новая'),
        ('в прогрессе', 'В прогрессе'),
        ('завершен', 'Завершен')
    ]

    title = models.CharField(max_length=100, blank=False, null=False, default="Без названия")
    description = models.TextField(blank=True, null=True, default="")

    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="новая")
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='project_reporter')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True)


class Task(models.Model):
    STATUS_CHOICES = [
        ('новая', 'Новая'),
        ('в прогрессе', 'В прогрессе'),
        ('завершен', 'Завершен')
    ]
    TYPE_CHOICES = [
        ('epic', 'Epic'),
        ('story', 'Story'),
        ('task', 'Task')
    ]

    title = models.CharField(max_length=100, blank=False, null=False, default="Без названия")
    description = models.TextField(blank=True, null=True, default="")
    type = models.CharField(max_length=100, choices=TYPE_CHOICES, default="project")

    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="новая")
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='task_reporter')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='task_assigned_to')
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)