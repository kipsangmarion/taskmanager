from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import UserProfile, Task, Activity, Comment
from .serializers import UserProfileSerializer, TaskSerializer, ActivitySerializer, CommentSerializer


class UserProfileAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.user_profile = UserProfile.objects.create(user=self.user, intro='Test intro')

        self.create_url = reverse('user-profile-list-create')
        self.detail_url = reverse('user-profile-detail', args=[self.user_profile.id])
        self.login_url = reverse('token_obtain_pair')

        self.login_data = {
            'username': 'testuser',
            'password': 'testpassword'
        }

        self.token_response = self.client.post(self.login_url, self.login_data, format='json')
        self.access_token = self.token_response.data['access']

    def test_create_user_profile(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        data = {
            'intro': 'New intro',
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserProfile.objects.count(), 2)  # 1 existing + 1 new profile
        self.assertEqual(response.data['intro'], 'New intro')

    def test_retrieve_user_profile(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['intro'], 'Test intro')

    def test_update_user_profile(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        data = {
            'intro': 'Updated intro',
        }
        response = self.client.patch(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['intro'], 'Updated intro')


class TaskAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.task = Task.objects.create(
            user=self.user,
            title='Test Task',
            tag='UI',
            desc='Test description',
            status='NEW',
            hours=5.0,
            planned_start_date='2023-07-31T10:00:00Z',
            planned_end_date='2023-07-31T15:00:00Z',
            actual_start_date='2023-07-31T11:00:00Z',
            actual_end_date='2023-07-31T14:00:00Z',
            content='Test content',
        )

        self.create_url = reverse('task-list-create')
        self.detail_url = reverse('task-detail', args=[self.task.id])
        self.login_url = reverse('token_obtain_pair')

        self.login_data = {
            'username': 'testuser',
            'password': 'testpassword'
        }

        self.token_response = self.client.post(self.login_url, self.login_data, format='json')
        self.access_token = self.token_response.data['access']

    def test_create_task(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        data = {
            'title': 'New Task',
            'tag': 'UI',
            'desc': 'New description',
            'status': 'NEW',
            'hours': 3.0,
            'planned_start_date': '2023-07-31T12:00:00Z',
            'planned_end_date': '2023-07-31T17:00:00Z',
            'actual_start_date': '2023-07-31T13:00:00Z',
            'actual_end_date': '2023-07-31T16:00:00Z',
            'content': 'New content',
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)  # 1 existing + 1 new task
        self.assertEqual(response.data['title'], 'New Task')

    def test_retrieve_task(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Task')

    def test_update_task(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        data = {
            'title': 'Updated Task',
            'status': 'INPROGRESS',
            'hours': 8.0,
        }
        response = self.client.patch(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Task')
        self.assertEqual(response.data['status'], 'INPROGRESS')
        self.assertEqual(response.data['hours'], 8.0)

    def test_delete_task(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

# Add more test cases for the Activity and Comment APIs in a similar manner.

