from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import BankAccountSerializer
from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from bank.models import Account

# Create your views here.

class BankAccountViewsets(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = BankAccountSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]