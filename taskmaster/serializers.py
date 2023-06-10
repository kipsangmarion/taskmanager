from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers

from taskmaster.models import UserProfile, Task, Tag, Activity, Comment


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


# Register serializer
class RegisterSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'firstname', 'lastname')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        if attrs['username'] is None:
            raise serializers.as_serializer_error()

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'],
                                        validated_data['firstname'], validated_data['lastname'])

        return user


# Login Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


# UserProfileSerializer
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


# TaskSerializer
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


# TagSerializer
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


# ActivitySerializer
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


# CommentSerializer
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
