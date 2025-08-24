from rest_framework import serializers
from .models import Task

class TaskListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'title', 'due_date', 'status', 'created_at', 'updated_at', 'priority']


class TaskDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'title', 'due_date', 'status', 'created_at', 'updated_at', 'priority', 'description']


