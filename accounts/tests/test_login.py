import pytest
from rest_framework import status
from accounts.models import User
from django.urls import reverse


class TestLoginView:
    def test_login_user_success(self, api_client, user_instance):
        url = reverse('login')
        payload = {
            'email': user_instance.email,
            'password':'12345678',
        }

        response = api_client.post(url, data=payload)
        assert response.status_code == status.HTTP_200_OK
        assert 'access' in response.data
        assert 'refresh' in response.data

    def test_login_user_wrong_password(self, api_client, user_instance):
        url = reverse('login')
        payload={
            'email':user_instance.email,
            'password':'123',
        }

        response = api_client.post(url, data=payload)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert 'access' not in response.data
        assert 'refresh' not in response.data