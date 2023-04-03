from .base import BaseClass
from django.db import models
from django.conf import settings
# from django.utils.text import slugify
from pytils.translit import slugify


class Project(BaseClass):
    name = models.CharField(max_length=100, null=False)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    description = models.TextField(blank=True)
    # customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='projects')
    
    

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
