from django.db import models

from django.conf import settings
from base.models import GenericBaseModel,State

User =settings.AUTH_USER_MODEL
# Create your models here.
class Task(GenericBaseModel):
    title = models.CharField(max_length=100)
    STATE_CHOICES = [
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    ]
    PRIORITY_CHOICES= [
        ("low","Low"),
        ("medium","Medium"),
        ("high","High")
    ]
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default="medium")
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default="pending")
    start_date= models.DateTimeField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="assigned_tasks"
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="created_tasks"
    )

    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="updated_tasks"
    )


    def __str__(self):
        return self.title