from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from base.models import BaseModel
from department.models import Department


class UserManager(BaseUserManager):
    def create_user(self, email_address, password=None, **extra_fields):
        if not email_address:
            raise ValueError("The Email Address must be set")
        email_address = self.normalize_email(email_address)
        user = self.model(email_address=email_address, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email_address, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email_address, password, **extra_fields)

    def get_by_natural_key(self, email_address):
        return self.get(email_address=email_address)


class User(AbstractBaseUser, BaseModel):
    email_address = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    department = models.CharField(
        max_length=100,
        blank=True,
        default="Dime",
    )

    USERNAME_FIELD = "email_address"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email_address