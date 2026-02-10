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
    message = models.TextField()

    notification_type = models.ForeignKey(State, on_delete=models.CASCADE
    )

    state = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
        related_name="notifications_by_state"
    )

    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
