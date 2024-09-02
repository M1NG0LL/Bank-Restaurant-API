from django import forms
from .models import Reservation

# Create your forms here.

class Make_Reservation(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'maindish', 'dessert', 'drink']
        
class Login_to_Reservation(forms.Form):
    id = forms.CharField(max_length=100)

class Get_Bank_Account(forms.Form):
    id = forms.CharField(max_length=100)
    password = forms.CharField(max_length=50)