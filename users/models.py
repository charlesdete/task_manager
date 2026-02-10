from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from base.models import BaseModel


class User(AbstractBaseUser,BaseModel, PermissionsMixin):
    email_address = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)



    USERNAME_FIELD = "email_address"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email_address
    
    