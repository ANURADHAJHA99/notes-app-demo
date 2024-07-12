from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Note

class UserTests(APITestCase):

    def test_create_user(self):
        url = reverse('user_create')
        data = {'username': 'testuser', 'password': 'testpass123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

    def test_obtain_token(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        url = reverse('api_token_auth')
        data = {'username': 'testuser', 'password': 'testpass123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

class NoteTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.login(username='testuser', password='testpass123')
        self.token_url = reverse('api_token_auth')
        self.token_response = self.client.post(self.token_url, {'username': 'testuser', 'password': 'testpass123'}, format='json')
        self.token = self.token_response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

    def test_create_note(self):
        url = reverse('note_list_create')
        data = {'title': 'Test Note', 'body': 'This is a test note.'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Note.objects.count(), 1)
        self.assertEqual(Note.objects.get().title, 'Test Note')

    def test_list_notes(self):
        Note.objects.create(user=self.user, title='Test Note', body='This is a test note.')
        url = reverse('note_list_create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Note')

    def test_retrieve_note(self):
        note = Note.objects.create(user=self.user, title='Test Note', body='This is a test note.')
        url = reverse('note_detail', args=[note.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Note')

    def test_update_note(self):
        note = Note.objects.create(user=self.user, title='Test Note', body='This is a test note.')
        url = reverse('note_detail', args=[note.id])
        data = {'title': 'Updated Test Note', 'body': 'This is an updated test note.'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Note.objects.get().title, 'Updated Test Note')

    def test_delete_note(self):
        note = Note.objects.create(user=self.user, title='Test Note', body='This is a test note.')
        url = reverse('note_detail', args=[note.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Note.objects.count(), 0)
