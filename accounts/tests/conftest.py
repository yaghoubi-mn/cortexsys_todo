from rest_framework.test import APIClient
import pytest
from accounts.models import User

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user_instance(db):
    user = User(username='test2435', email='test@test2.com')
    user.set_password('12345678')
    user.save()
    return user