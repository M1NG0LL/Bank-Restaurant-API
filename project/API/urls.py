from django.urls import path, include
from . import views 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Bank_Accounts', views.BankAccountViewsets, basename='bankaccount')

urlpatterns = [
    path('viewsets/', include(router.urls)),

    path('api-auth', include('rest_framework.urls')),
]
