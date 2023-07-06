from django.urls import path

from taskmaster.user_profile_view import UserProfileCreateAPIView, UserProfileRetrieveUpdateDestroyAPIView
from taskmaster.tag_view import TagCreateAPIView, TagRetrieveUpdateDestroyAPIView
from taskmaster.task_view import TaskCreateAPIView, TaskRetrieveUpdateDestroyAPIView
from taskmaster.activity_view import ActivityCreateAPIView, ActivityRetrieveUpdateDestroyAPIView
from taskmaster.comment_view import CommentCreateAPIView, CommentRetrieveUpdateDestroyAPIView
from taskmaster.views import RegisterAPI, ChangePasswordAPI, LogoutAPI, LogoutAllAPI
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterAPI.as_view(), name='auth_register'),
    path('change_password/<int:pk>/', ChangePasswordAPI.as_view(), name='auth_change_password'),
    path('logout/', LogoutAPI.as_view(), name='auth_logout'),
    path('logout_all/',LogoutAllAPI.as_view(), name='auth_logout_all'),

    # UserProfileView
    path('userprofile/', UserProfileCreateAPIView.as_view(), name='user-profile-list-create'),
    path('userprofile/<int:pk>/', UserProfileRetrieveUpdateDestroyAPIView.as_view(), name='user-profile-detail'),

    # TagView
    path('tag/', TagCreateAPIView.as_view(), name='tag-list-create'),
    path('tag/<int:pk>/', TagRetrieveUpdateDestroyAPIView.as_view(), name='tag-detail'),

    # TaskView
    path('task/', TaskCreateAPIView.as_view(), name='task-list-create'),
    path('task/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task-list-detail'),

    # ActivityView
    path('activity/', ActivityCreateAPIView.as_view(), name='activity-list-create'),
    path('activity/<int:pk>/', ActivityRetrieveUpdateDestroyAPIView.as_view(), name='activity-detail'),

    # CommentView
    path('comment/', CommentCreateAPIView.as_view(), name='comment-list-create'),
    path('comment/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view(), name='comment-detail'),
]
