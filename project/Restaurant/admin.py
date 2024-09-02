from django.contrib import admin
from .models import MainDish, Dessert, Drink, Reservation

# Register your models here.

admin.site.register(MainDish)
admin.site.register(Dessert)
admin.site.register(Drink)
admin.site.register(Reservation)