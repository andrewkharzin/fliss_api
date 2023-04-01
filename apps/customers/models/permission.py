from django.db import models
from django.contrib.auth.models import AbstractUser

class Permission(models.Model):
    name = models.CharField(max_length=50)
    codename = models.CharField(max_length=50)