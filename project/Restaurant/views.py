from django.shortcuts import render, redirect
from django.urls import reverse
from .models import MainDish, Dessert, Drink, Reservation
from .forms import Make_Reservation, Login_to_Reservation, Get_Bank_Account


from bank.utils import sending_email
from bank.models import Account

# Create your views here.

def make_reservation(request):
    if request.method == "POST":
        form = Make_Reservation(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email']
            
            if Reservation.objects.filter(email=email):
                return render(request, 'restaurant/make.html', {'form': form, 'error': 'There is an account with the same Email.'})
            form.save()
            
            reservation = Reservation.objects.get(email=email)
            
            maindish = reservation.maindish
            dessert = reservation.dessert
            drink = reservation.drink

            reservation.total_cash += (maindish.price + dessert.price + drink.price)
            
            reservation.save()
            
            # send mail
            message = f'''Welcome Mr.{reservation.name} \
                \nThanks for making Reservation with our Restaurant. \
                    \nThis is Your ID to enter the Reservation: "{reservation.id}". '''
            
            sending_email(email, message)
            
            return redirect('enter_reservation')
            
    else:
        form = Make_Reservation()
            
    return render(request, 'restaurant/make.html', {'form': form})

def enter_reservation(request):
    if request.method == "POST":
        form = Login_to_Reservation(request.POST)
        
        if form.is_valid():
            id = form.cleaned_data['id']
            
            if Reservation.objects.filter(id=id):
                return redirect(reverse('home', kwargs={'id': id}))
            else:
                return render(request, 'restaurant/enter.html', {'form': form, \
                        'error': "Wrong ID, Please Enter a real one."})
            
    else:
        form = Login_to_Reservation()
            
    return render(request, 'restaurant/enter.html', {'form': form})

def home(request, id):
    
    if id:
        reservation = Reservation.objects.get(id = id)
        return render(request, 'restaurant/home.html', {'reservation': reservation})
    
    return redirect('enter_reservation')

def logout(request, id):
    if id:
        reservation = Reservation.objects.get(id = id)
        return render(request, 'restaurant/logout.html', {'reservation': reservation})
    
    return redirect('enter_reservation')

# Paymet

def pay_by_bank(request, id):
    try:
        form = Get_Bank_Account(request.POST)
        reservation = Reservation.objects.get(id=id)
        
        if form.is_valid():
            bank_id = form.cleaned_data['id']
            password = form.cleaned_data['password']
            
            if Account.objects.filter(id=bank_id, password=password):
                account = Account.objects.get(id=bank_id)
                
                account.balance -= reservation.total_cash
                
                account.save()
                
                # send email
                message = f'''Welcome Mr.{reservation.name} \
                    \nThere is an amount of money = {reservation.total_cash}, has been taken from your Account. \
                        \nBy paying Reservation of a restaurant.'''
                        
                sending_email(account.email, message)
                
                reservation.delete()
                
                return redirect('enter_reservation')
            else:
                return render(request, 'restaurant/payment.html', {'form': form, 'error': "Account isn't found"})
    
    except Exception as e:
        return redirect('enter_reservation')
            
    return render(request, 'restaurant/payment.html', {'form': form, 'reservation': reservation})

def pay_by_cash(request, id):
    if id:
        reservation = Reservation.objects.get(id=id)
        reservation.delete()
    
    return redirect('enter_reservation')