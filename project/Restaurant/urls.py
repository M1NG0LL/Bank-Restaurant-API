from django.urls import path
from . import views

urlpatterns = [
    path('Make_Reservation', views.make_reservation, name="make_reservation"),
    path('Enter_Reservation', views.enter_reservation, name="enter_reservation"),
    path('home/<str:id>', views.home, name="home"),
    path('logout/<str:id>', views.logout, name="logout"),
    
    # Paymet
    path('Pay_by_Bank/<str:id>', views.pay_by_bank, name="pay_by_bank"),
    path('Pay_by_Cash/<str:id>', views.pay_by_cash, name="pay_by_cash"),
]
