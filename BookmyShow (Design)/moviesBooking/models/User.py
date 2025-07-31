from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


class User(AbstractBaseUser):
    first_name = models.CharField(null=True, blank=True, max_length=255)
    last_name = models.CharField(null=True, blank=True, max_length=255)
    email = models.EmailField(unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'  # ✅ Required
    REQUIRED_FIELDS = ['first_name', 'last_name']  # ✅ Optional, used by createsuperuser

    def __str__(self):
        return self.email
