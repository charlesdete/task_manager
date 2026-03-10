# notification/models.py
from django.db import models
from django.conf import settings
from base.models import GenericBaseModel, State
User = settings.AUTH_USER_MODEL

class Notification(GenericBaseModel):

   

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notifications",
        blank=True,
        null=True
    )

    title = models.CharField(max_length=255)
    message = models.CharField(max_length=255)

    NOTIFICATION_TYPE_CHOICES = [
        ("info", "Info"),
        ("warning", "Warning"),
        ("success", "Success"),
        ("error", "Error"),
    ]
    notification_type = models.CharField( 
        max_length=20,
        choices=NOTIFICATION_TYPE_CHOICES,
        default="info"
    )

    state = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
        related_name="notifications_state",
        blank=True,
        null=True
    )

    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
