from django.http import StreamingHttpResponse
from django.shortcuts import render, redirect
from rest_framework import viewsets

from .models import Customers
from .serializers import RegisterSerializer


# Create your views here.

def home(request):
    return render(request, 'home.html')

def payments(request):
    return render(request, 'payments.html')

def profile(request):
    return render(request, 'profile.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

class CustomerViewSet (viewsets.ModelViewSet):
    queryset = Customers.objects.all().order_by('first_name')
    serializer_class = RegisterSerializer



