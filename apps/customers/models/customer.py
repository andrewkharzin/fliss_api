from django.db import models
from apps.users.models import User

class Tenant(models.Model):
    name = models.CharField(max_length=50)
    schema_name = models.CharField(max_length=50)

class CustomerManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.schema_name = None
        super().__init__(*args, **kwargs)

    def set_schema_name(self, schema_name):
        self.schema_name = schema_name

    def get_queryset(self):
        if self.schema_name is not None:
            return super().get_queryset().using(self.schema_name)
        else:
            return super().get_queryset()

class Customer(User):
    company_name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    tenant_id = models.IntegerField()
    roles = models.ManyToManyField('Role')
    
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    
    objects = CustomerManager()