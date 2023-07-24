from django.db.models import Q
from rest_framework import generics
from taskmaster.models import Task
from taskmaster.serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated


class TaskCreateAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        tag = self.request.query_params.get('tag')
        status = self.request.query_params.get('status')
        filters = Q()
        # Filter by tag and status if provided
        if tag:
            filters &= Q(tag=tag)
        if status:
            filters &= Q(status=status)

        return queryset.filter(filters).distinct()


class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = Task
