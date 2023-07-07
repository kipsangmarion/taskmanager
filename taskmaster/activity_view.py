from rest_framework import generics
from taskmaster.models import Activity
from taskmaster.serializers import ActivitySerializer
from rest_framework.permissions import IsAuthenticated


class ActivityCreateAPIView(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ActivitySerializer


class ActivityRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activity.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ActivitySerializer
