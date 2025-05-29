from rest_framework import permissions, status
from  rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.projects.models import Task
from apps.projects.serializers import TaskSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def task_display(request, task_id):
    task = Task.objects.get(id=task_id)
    if task is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TaskSerializer(task)
    return Response({'task': serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def task_create(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def task_delete(request, task_id):
    task = Task.objects.get(id=task_id)
    if task is None:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if task.assigned_to != request.user and task.reporter != request.user:
        return Response({'error': 'Not authorized to delete this task'}, status=status.HTTP_403_FORBIDDEN)

    task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def task_update(request, task_id):
    task = Task.objects.get(id=task_id)
    if task is None:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TaskSerializer(task, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
