from django.db import models
from django.contrib.auth.models import AbstractUser
from base.models import Profile


class User(AbstractUser):
    profiles = models.ManyToManyField(Profile, blank=True)
    email = models.EmailField(null=True, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []




