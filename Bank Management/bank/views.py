from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import Signup, Login, Get_balance
from .models import Account

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = Signup(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email']
            
            if Account.objects.filter(email = email).exists():
                return render(request, 'signup.html', {'form': form, 'error': 'There is an account with the same Email.'})
                
            else:
                if form.cleaned_data['password'] == form.cleaned_data['password_confirmation']:
                    form.save()
                    account = Account.objects.get()
                    
                    #send email to auth
                    # email_auth()
                    
                    return redirect('login')
                    
                else:
                    return render(request, 'signup.html', {'form': form, 'error': "password isn't same as confirmation password."})
    else:
        form = Signup()
    
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == "POST":
        form = Login(request.POST)
        
        if form.is_valid():
            id = form.cleaned_data['id']
            
            if Account.objects.filter(id = id).exists():
                account = Account.objects.get(id = id)
                
                if account.is_active:
                    return redirect(reverse('login_page', kwargs={'id': id}))
                else:
                    return render(request, 'login.html', {'form': form, \
                        'error': "Account isn't active. \n please active it from your email."})
            
            else:
                return render(request, 'login.html', {'form': form, 'error': "Account isn't found"})
    else:
        form = Login()
        
    return render(request, 'login.html', {'form': form})

def login_page(request, id):
    
    if id:
        account = Account.objects.get(id = id)
        return render(request, 'login_page.html', {'account': account})
    
    return redirect('login')

def logout(request, id):
    
    if id:
        account = Account.objects.get(id = id)
        return render(request, 'logout.html', {'account': account})
    
    return redirect('login')

# def email_auth(request):
#     return render(request, 'email_auth.html')

#Functions ====================================

def deposit(request, id):
    
    form = Get_balance(request.POST)
    account = Account.objects.get(id = id)
    
    if form.is_valid():
        amount = form.cleaned_data['amount']
        account.balance += amount
        account.save()
        
        return redirect(reverse('login_page', kwargs={'id': id}))
        
    return render(request, 'functions/deposit.html', {'form': form, 'account': account})

def withdraw(request, id):
    
    form = Get_balance(request.POST)
    account = Account.objects.get(id = id)
    
    if form.is_valid():
        amount = form.cleaned_data['amount']
        account.balance -= amount
        account.save()
        
        return redirect(reverse('login_page', kwargs={'id': id}))
        
    return render(request, 'functions/withdraw.html', {'form': form, 'account': account})

def show_info(request, id):
    account = Account.objects.get(id = id)
    
    return render(request, 'functions/show_info.html', {'account': account})