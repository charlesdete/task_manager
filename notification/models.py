# notification/models.py
from django.db import models
from django.conf import settings
from base.models import GenericBaseModel, State
User = settings.AUTH_USER_MODEL

class Notification(GenericBaseModel):

   

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notifications"
    )

    title = models.CharField(max_length=255)
    message = models.CharField(max_length=255)

    notification_type = models.ForeignKey(State, on_delete=models.CASCADE,blank=True
    )

    state = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
        related_name="notifications_state",
        blank=True
    )

    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
