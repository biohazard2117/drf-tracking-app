from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from todo.models import Todo


class TestListCreateTodos(APITestCase):

    def authenticate(self):
        sample_user = {"username": "TestUser",
                       "email": "test@gmail.com", "password": "test123!@"}
        self.client.post(reverse("register"), sample_user)
        response = self.client.post(
            reverse("login"), {"email": "test@gmail.com", "password": "test123!@"})
        
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {response.data['token']}")

    def test_should_not_create_todo_with_no_auth(self):
        sample_todo = {'title': 'Testing1',
                       'description': 'Testing Description'}
        response = self.client.post(reverse('todo'), sample_todo)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_should_create_todo(self):
        previous_todo_count = Todo.objects.all().count()
        self.authenticate()
        sample_todo = {'title': 'Testing1',
                       'description': 'Testing Description'}
        response = self.client.post(reverse('todo'), sample_todo)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Todo.objects.all().count(), previous_todo_count+1)
        self.assertEqual(response.data['title'],'Testing1')
        self.assertEqual(response.data['description'],'Testing Description')

