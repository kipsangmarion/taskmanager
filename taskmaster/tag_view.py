from rest_framework import generics
from taskmaster.models import Tag
from taskmaster.serializers import TagSerializer
from rest_framework.permissions import IsAuthenticated


class TagCreateAPIView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = TagSerializer


class TagRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = TagSerializer
