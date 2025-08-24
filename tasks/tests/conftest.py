from rest_framework.test import APIClient
import pytest
from accounts.models import User
from tasks.models import Task

@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def authenticated_api_client(api_client, user_instance):    
    api_client.force_authenticate(user=user_instance)
    return api_client


@pytest.fixture
def user_instance(db):
    user = User(username='test2435', email='test@test2.com')
    user.set_password('12345678')
    user.save()
    return user


@pytest.fixture
def task_instance(db, user_instance):
    return Task.objects.create(
        title='test',
        description='test des',
        status='pending',
        due_date='2000-1-1',
        priority=1,
        owner=user_instance,
    )