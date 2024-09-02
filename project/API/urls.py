from django.urls import path, include
from . import views 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Bank_Accounts', views.BankAccountViewsets, basename='bankaccount')

router.register('Restaurant/Maindish', views.MainDishViewsets, basename='Maindish')
router.register('Restaurant/Dessert', views.DessertViewsets, basename='Dessert')
router.register('Restaurant/Drink', views.DrinkViewsets, basename='Drink')
router.register('Restaurant/Reservation', views.ReservationViewsets, basename='Reservation')

urlpatterns = [
    path('signup/', views.signup),
    path('My_token/', views.my_token),
    
    path('viewsets/', include(router.urls)),

    path('api-auth', include('rest_framework.urls')),
]
