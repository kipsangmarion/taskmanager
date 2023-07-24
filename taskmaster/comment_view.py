from django.db.models import Q
from rest_framework import generics
from taskmaster.models import Comment
from taskmaster.serializers import CommentSerializer


class CommentCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        task = self.request.query_params.get('task')
        activity = self.request.query_params.get('activity')
        filters = Q()
        # Filter by tag and status if provided
        if task:
            filters &= Q(task=task)
        if activity:
            filters &= Q(activity=activity)

        return queryset.filter(filters).distinct()


class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
