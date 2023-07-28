from rest_framework import generics
from taskmaster.models import UserProfile
from taskmaster.serializers import UserProfileSerializer


class UserProfileCreateAPIView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_object(self):
        # Return the UserProfile instance of the currently logged-in user
        return self.request.user.user_in_profile


class UserProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_object(self):
        # Retrieve and return the UserProfile instance of the currently logged-in user
        return self.request.user.user_in_profile


