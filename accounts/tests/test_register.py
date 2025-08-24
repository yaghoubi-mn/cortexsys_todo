import pytest
from rest_framework import status
from accounts.models import User
from django.urls import reverse

@pytest.mark.django_db
class TestRegisterView:
    def test_register_user_success(self, api_client):
        url = reverse('register')
        payload = {
            'username': 'test1',
            'password': '12345678',
            'email':'test1@test.com'
        }

        response = api_client.post(url, data=payload)
        assert response.status_code == status.HTTP_201_CREATED
        assert User.objects.filter(username=payload['username']).exists()

    def test_register_username_already_exists(self, api_client, user_instance):
        url = reverse('register')
        payload = {
            'username': user_instance.username,
            'email':'test2@test.com',
            'password':'12345678'
        }

        response = api_client.post(url, data=payload)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_register_user_email_already_exists(self, api_client, user_instance):
        url = reverse('register')
        payload = {
            'username': 'test325',
            'email':user_instance.email,
            'password':'12345678'
        }

        response = api_client.post(url, data=payload)
        assert response.status_code == status.HTTP_400_BAD_REQUEST