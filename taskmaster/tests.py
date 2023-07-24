from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from rest_framework.test import force_authenticate
from taskmaster.models import Task
from taskmaster.serializers import TaskSerializer
from taskmaster.task_view import TaskCreateAPIView, TaskRetrieveUpdateDestroyAPIView


class TaskAPIViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.task_data = {'title': 'Sample Task', 'desc': 'Sample Description', 'tag': 'Sample Tag'}
        self.task = Task.objects.create(title='Sample Task', desc='Sample Description', tag='Sample Tag')

    def test_task_create_api_view(self):
        # Create a request with task data
        request = self.factory.post('/tasks/', self.task_data)
        force_authenticate(request, user=self.user)

        # Set up the view and create the task
        view = TaskCreateAPIView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 201)

        # Check that the task is created in the database
        task = Task.objects.last()
        self.assertEqual(task.title, self.task_data['title'])
        self.assertEqual(task.description, self.task_data['description'])
        self.assertEqual(task.tag, self.task_data['tag'])

    def test_task_retrieve_update_destroy_api_view(self):
        # Create a request to retrieve the task
        request = self.factory.get(f'/tasks/{self.task.id}/')
        force_authenticate(request, user=self.user)

        # Set up the view and retrieve the task
        view = TaskRetrieveUpdateDestroyAPIView.as_view()
        response = view(request, pk=self.task.id)
        self.assertEqual(response.status_code, 200)

        # Check that the retrieved task matches the created task
        self.assertEqual(response.data['title'], self.task.title)
        self.assertEqual(response.data['description'], self.task.description)
        self.assertEqual(response.data['tag'], self.task.tag)

        # Create a request to update the task
        updated_data = {'title': 'Updated Task', 'description': 'Updated Description', 'tag': 'Updated Tag'}
        request = self.factory.put(f'/tasks/{self.task.id}/', updated_data)
        force_authenticate(request, user=self.user)

        # Set up the view and update the task
        view = TaskRetrieveUpdateDestroyAPIView.as_view()
        response = view(request, pk=self.task.id)
        self.assertEqual(response.status_code, 200)

        # Check that the task is updated in the database
        task = Task.objects.get(pk=self.task.id)
        self.assertEqual(task.title, updated_data['title'])
        self.assertEqual(task.description, updated_data['description'])
        self.assertEqual(task.tag, updated_data['tag'])

        # Create a request to delete the task
        request = self.factory.delete(f'/tasks/{self.task.id}/')
        force_authenticate(request, user=self.user)

        # Set up the view and delete the task
        view = TaskRetrieveUpdateDestroyAPIView.as_view()
        response = view(request, pk=self.task.id)
        self.assertEqual(response.status_code, 204)

        # Check that the task is deleted from the database
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(pk=self.task.id)
