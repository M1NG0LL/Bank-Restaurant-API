from django.db import models
import uuid

# Create your models here.

class Account(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    password = models.CharField(max_length=50)
    password_confirmation = models.CharField(max_length=50)
    
    balance = models.DecimalField(max_digits=100, decimal_places=2, default=0.0)
    is_active = models.BooleanField(default=False)
    