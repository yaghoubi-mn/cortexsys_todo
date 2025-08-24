import pytest
from rest_framework import status
from django.urls import reverse
import json
from tasks.models import Task

@pytest.mark.django_db
class TestTaskView:
    def test_create_task_success(self, authenticated_api_client, user_instance):
        url = reverse('task-list')
        payload ={
            'title':'test',
            'description':'testdfd f',
            'status':'pending',
            'due_date':'2000-1-1',
            'priority':1
        }
        response = authenticated_api_client.post(url, data=payload)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['title'] == payload['title']
        assert Task.objects.filter(title=payload['title'], owner=user_instance).exists()

    def test_create_task_unauthenticated(self, api_client, user_instance    ):
        url = reverse('task-list')
        payload ={
            'title':'test',
            'description':'testdfd f',
            'status':'pending',
            'due_date':'2000-1-1',
            'priority':1
        }
        response = api_client.post(url, data=payload)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert not Task.objects.filter(title=payload['title'], owner=user_instance).exists()
    
    def test_get_task_list_success(self, authenticated_api_client, user_instance):
        url = reverse('task-list')
        response = authenticated_api_client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_get_task_list_unauthenticated(self, api_client):
        url = reverse('task-list')
        response = api_client.get(url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_get_task_detail_success(self, authenticated_api_client, task_instance):
        url = reverse('task-detail', args=[task_instance.id])
        response = authenticated_api_client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_get_task_detail_unauthenticated(self, api_client, task_instance):
        url = reverse('task-detail', args=[task_instance.id])
        response = api_client.get(url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_update_task_success(self, authenticated_api_client, task_instance):
        url = reverse('task-detail', args=[task_instance.id])
        payload ={
            'title':'updated test',
            'description':'te dfstdfd f',
            'status':'complete',
            'due_date':'2000-1-2',
            'priority':2
        }
        response = authenticated_api_client.put(url, data=payload)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == payload['title']
        task_instance.refresh_from_db()
        assert task_instance.title == payload['title']

    def test_update_task_unauthenticated(self, api_client, task_instance):
        url = reverse('task-detail', args=[task_instance.id])
        payload ={
            'title':'updaed test',
            'description':'td estdfd f',
            'status':'pending',
            'due_date':'2000-1-1',
            'priority':2
        }
        response = api_client.put(url, data=payload)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_delete_task_success(self, authenticated_api_client, task_instance):
        url = reverse('task-detail', args=[task_instance.id])
        response = authenticated_api_client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Task.objects.filter(pk=task_instance.pk).exists()

    def test_delete_task_unauthenticated(self, api_client, task_instance):
        url = reverse('task-detail', args=[task_instance.id])
        response = api_client.delete(url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED