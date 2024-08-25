from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import Signup, Login, Get_balance, code_collector, Pass_reset_knower, Pass_reset
from .models import Account
from .utils import sending_email, random_code

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
                    account = Account.objects.get(email = email)
                    
                    #send email
                    code = random_code()
                    account.code_confirm = code
                    account.save()
                    
                    message = f'''Welcome Mr.{account.name} \n\
                        Your ID = "{account.id}" \n\
                            Thank you for signing up! To complete your registration, please verify your email address by copying this code '{account.code_confirm}' and use it to activate your email.
                                '''
                
                    sending_email(email, message)
                    
                    return redirect(reverse('account_activate', kwargs={'email': email}))
                    
                else:
                    return render(request, 'signup.html', {'form': form, 'error': "password isn't same as confirmation password."})
    else:
        form = Signup()
    
    return render(request, 'signup.html', {'form': form})

# account activation
def resend_activation_code(request, email):
    try:
        account = Account.objects.get(email=email)
        
        code = random_code()
        account.code_confirm = code
        account.save()
        
        sending_email(email, "Your new activation code is: " + code)
        
        return redirect(reverse('account_activate', kwargs={'email': email}))
    
    except Account.DoesNotExist:
        return redirect('login')

def account_activate(request, email):
    try: 
        account = Account.objects.get(email=email)
        
        if request.method == "POST":
            form = code_collector(request.POST)
            
            if form.is_valid():
                code = form.cleaned_data['code']

                if code == account.code_confirm:
                    account.is_active = True
                    account.save()
                    return redirect('login')
                else:
                    return render(request, 'account_activate.html', {'form': form,'account': account,\
                        'error': "Wrong code. Please check your email."})
                    
        else:
            form = code_collector()
    
    except Exception as e:
        return redirect('login')

    return render(request, 'account_activate.html', {'form': form, 'account': account})

# account activation

def login(request):
    if request.method == "POST":
        form = Login(request.POST)
        
        if form.is_valid():
            id = form.cleaned_data['id']
            password = form.cleaned_data['password']
            
            if Account.objects.filter(id = id, password = password).exists():
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

# pass reset

def pass_reset_knower(request):
    if request.method == "POST":
        form = Pass_reset_knower(request.POST)
        
        if form.is_valid():
            id = form.cleaned_data['id']
            email = form.cleaned_data['email']
            
            if Account.objects.filter(id = id, email = email):
                account = Account.objects.get(id = id)
                
                code = random_code()
                account.code_confirm = code
                account.save()
                
                message = f'''
                Welcome Mr.{account.name} \n\
                You requested a reset password, This is the code '{account.code_confirm}'. 
                '''
                
                sending_email(account.email, message)
                
                
                return redirect(reverse('pass_reset_code_enter', kwargs={'id': id}))
            else:
                return render(request, 'pass_reset_knower.html', {'form': form, 'error': "Account isn't found"})
        
    else:
        form = Pass_reset_knower()
    
    return render(request, 'pass_reset/pass_reset_knower.html', {'form': form})

def pass_reset_code_enter(request, id):
    form = code_collector()

    try: 
        account = Account.objects.get(id=id)
        
        if request.method == "POST":
            form = code_collector(request.POST)
            if form.is_valid():
                code = form.cleaned_data['code']
                if code == account.code_confirm:
                    return redirect(reverse('pass_reset', kwargs={'id': id}))
                else:
                    return render(request, 'pass_reset_code_enter.html', {'form': form,'account': account,\
                        'error': "Wrong code. Please check your email."})
       
    except Exception as e:
        return redirect('pass_reset_knower')
    
    return render(request, 'pass_reset/pass_reset_code_enter.html', {'form': form, 'account': account})

def pass_reset(request, id):
    form = Pass_reset()
    
    try:
        account = Account.objects.get(id = id)
        
        if request.method == "POST":
            form = Pass_reset(request.POST)
            
            if form.is_valid():
                password = form.cleaned_data['password']
                password_confirmation = form.cleaned_data['password_confirmation']
                
                if password == password_confirmation:
                    account.password = password
                    account.password_confirmation = password_confirmation
                    account.save()
                    return redirect('login')
                else:
                    return render(request, 'pass_reset/pass_reset.html', {'form':form, \
                        'error': "The two password should be the same."})
        
    except Exception as e:
        return redirect('pass_reset_knower')
    
    return render(request, 'pass_reset/pass_reset.html', {'form':form})

# pass reset

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
        
        if amount > account.balance:
            return render(request, 'functions/withdraw.html', {'form': form, 'account': account, \
                'error': "The amount is more than your Balance."})
            
        else:
            account.balance -= amount
            account.save()
        
            return redirect(reverse('login_page', kwargs={'id': id}))
        
    return render(request, 'functions/withdraw.html', {'form': form, 'account': account})

def show_info(request, id):
    account = Account.objects.get(id = id)
    
    return render(request, 'functions/show_info.html', {'account': account})