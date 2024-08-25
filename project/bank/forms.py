from django import forms
from .models import Account

# Create your forms here.

class Signup(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'email', 'password', 'password_confirmation']
        
class Login(forms.Form):
    id = forms.CharField(max_length=100)
    password = forms.CharField(max_length=50)
        
class Get_balance(forms.Form):
    amount = forms.DecimalField(max_digits= 100, decimal_places=4)
    
class code_collector(forms.Form):
    code = forms.CharField(max_length=50, required=True)
    
class Pass_reset_knower(forms.Form):
    id = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100, required=True)
    
class Pass_reset(forms.Form):
    password = forms.CharField(max_length=50)
    password_confirmation = forms.CharField(max_length=50)