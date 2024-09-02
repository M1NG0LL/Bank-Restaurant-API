from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import *
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from bank.models import Account
from Restaurant.models import *

# Create your views here.

@api_view(["POST"])
def signup(request):

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        user = User.objects.get(username=request.data['username'])
        token = Token.objects.get(user=user)

        serializer = UserSerializer(user)

        data = {
            "user": serializer.data,
            "token": token.key
        }

        return Response(data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def my_token(request):
    
    data = request.data
    authenticate_user = authenticate(username=data['username'], password=data['password'])

    if authenticate_user is not None:
        user = User.objects.get(username=data['username'])
        serializer = UserSerializer(user)

        response_data = {
            'user': serializer.data,
        }

        token, created_token = Token.objects.get_or_create(user=user)

        if token:
            response_data['token'] = token.key
        elif created_token:
            response_data['token'] = created_token.key

        return Response(response_data)
    return Response({"detail": "not found"}, status=status.HTTP_400_BAD_REQUEST)

# API
class BankAccountViewsets(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = BankAccountSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    
class MainDishViewsets(viewsets.ModelViewSet):
    queryset = MainDish.objects.all()
    serializer_class = MainMealSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    
class DessertViewsets(viewsets.ModelViewSet):
    queryset = Dessert.objects.all()
    serializer_class = DessertSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    
class DrinkViewsets(viewsets.ModelViewSet):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    
class ReservationViewsets(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    
