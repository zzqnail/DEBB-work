from django.urls import path
from . import views, tasks

urlpatterns = [
    path('tasks/<int:task_id>/view/', tasks.task_display),
    path('tasks/create/', tasks.task_create),
    path('tasks/<int:task_id>/update/', tasks.task_update),
    path('tasks/<int:task_id>/delete/', tasks.task_delete),
]