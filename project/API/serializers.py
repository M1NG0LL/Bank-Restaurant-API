from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework.authtoken.models import Token

from Restaurant.models import *
from bank.models import Account

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        
    def save(self, **kwargs):

        new_user = User.objects.create_user(
            username = self.validated_data['username'],
            email = self.validated_data['email'],
            password= self.validated_data['password'],
        )

        new_user.save()

        new_token = Token.objects.create(user=new_user)
        
class BankAccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'name', 'email', 'password', 'password_confirmation', 'is_active']
        
class DessertSerializer(ModelSerializer):
    class Meta:
        model = Dessert
        fields = '__all__'

class MainMealSerializer(ModelSerializer):
    class Meta:
        model = MainDish
        fields = '__all__'

class DrinkSerializer(ModelSerializer):
    class Meta:
        model = Drink
        fields = '__all__'

class ReservationSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'