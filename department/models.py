from django.db import models
from base.models import GenericBaseModel,State
from django.conf import settings


class Department(GenericBaseModel):
    department_members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="departments",
        blank=True
    )
   

    def __str__(self):
        return self.name