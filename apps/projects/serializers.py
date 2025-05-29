from rest_framework import serializers

from debb_work.quickstart.serializers import UserSerializer
from .models import Task, Project

from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    assigned_to_id = serializers.IntegerField(write_only=True, required=False)
    assigned_to = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        assigned_to_id = validated_data.pop('assigned_to_id', None)

        task = Task.objects.create(**validated_data, reporter=user)
        assigned_to = User.objects.get(id=assigned_to_id)

        if assigned_to is not None:
            task.assigned_to = assigned_to

        task.save()
        return task

    def update(self, instance, validated_data):
        assigned_to_id = validated_data.pop('assigned_to_id', None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if assigned_to_id is not None or assigned_to_id=="":
            if assigned_to_id == "":
                instance.assigned_to = None
            else:
                instance.assigned_to = User.objects.get(id=assigned_to_id)

        instance.save()
        return instance