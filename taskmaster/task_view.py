from rest_framework import generics
from taskmaster.models import Task
from taskmaster.serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated


class TaskCreateAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = Task
