from django.db.models import Q
from rest_framework import generics
from taskmaster.models import Activity
from taskmaster.serializers import ActivitySerializer


class ActivityCreateAPIView(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        task = self.request.query_params.get('task')
        filters = Q()
        # Filter by tag
        if task:
            filters &= Q(task=task)

        return queryset.filter(filters).distinct()


class ActivityRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
