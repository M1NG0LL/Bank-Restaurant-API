from django.db import models
import uuid

# Create your models here.

class MainDish(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.CharField(max_length=250)
    price =  models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    
    def __str__(self):
        return f"Name= '{self.name}', Price= '{self.price}'"

class Dessert(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.CharField(max_length=250)
    price =  models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    
    def __str__(self):
        return f"Name= '{self.name}', Price= '{self.price}'"
    
class Drink(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.CharField(max_length=250)
    price =  models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    
    def __str__(self):
        return f"Name= '{self.name}', Price= '{self.price}'"
    
    
class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    maindish = models.OneToOneField(MainDish, related_name='reservation',  on_delete=models.SET_NULL, null=True)
    dessert = models.OneToOneField(Dessert, related_name='reservation',  on_delete=models.SET_NULL, null=True)
    drink = models.OneToOneField(Drink, related_name='reservation',  on_delete=models.SET_NULL, null=True)
    
    total_cash = models.DecimalField(max_digits=100, decimal_places=2, default=0.0)
    
    def __str__(self):
        return f"Name= '{self.name}', Email= '{self.email}', Total Cash= '{self.total_cash}'"