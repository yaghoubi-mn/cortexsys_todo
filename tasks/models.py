from django.db import models
from django.contrib.auth import get_user_model
from utils.validators import validate_title

User = get_user_model()


class Task(models.Model):
    title = models.CharField(max_length=200, validators=[validate_title])
    description = models.TextField(blank=True, default='')
    STATUS_CHOICES = (
        ('complete', 'Complete'),
        ('pending', 'Pending'),
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    due_date = models.DateField()
    priority = models.IntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
