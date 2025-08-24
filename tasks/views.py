from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Task
from .serializers import TaskDetailSerializer, TaskListSerializer
from .permisions import IsOwner
from .filters import TaskFilter

class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwner, permissions.IsAuthenticated]
    filterset_class = TaskFilter
    
    def get_serializer_class(self):
        if self.action == 'list':
            return TaskListSerializer
        return TaskDetailSerializer

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


