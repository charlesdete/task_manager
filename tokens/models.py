from django.db import models
from django.conf import settings
from django.utils import timezone
from base.models import GenericBaseModel, State

class Token(GenericBaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tokens"
    )
    key = models.CharField(max_length=255, unique=True)  # access token string
    refresh_key = models.CharField(max_length=255, unique=True, null=True, blank=True)
    expires_at = models.DateTimeField()
    revoked = models.BooleanField(default=False)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def is_expired(self):
        return timezone.now() >= self.expires_at

    def revoke(self):
        self.revoked = True
        self.save()

    def refresh(self, new_access, lifetime_minutes=15):
        self.key = new_access
        self.expires_at = timezone.now() + timezone.timedelta(minutes=lifetime_minutes)
        self.save()
        return self