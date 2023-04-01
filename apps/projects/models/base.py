from django.db import models


class BaseClass(models.Model):
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False, editable=False)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=True, editable=False)