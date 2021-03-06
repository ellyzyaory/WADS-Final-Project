from django.http import StreamingHttpResponse
from django.shortcuts import render, redirect
from rest_framework import viewsets

from django.http import StreamingHttpResponse
from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions, generics, status
from rest_framework.views import APIView
from .models import User, Transactions
from .serializers import UserSerializer, CreateUserSerializer, TransactionSerializer, LoginUserSerializer, User2Serializer
from django.contrib.auth import login
from knox.models import AuthToken
from knox.auth import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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

class UserView (generics.ListAPIView):
    # permission_classes = (IsAuthenticated,) 
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreateUserView(APIView):
    serializer_class = CreateUserSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            card_no = serializer.data.get('card_no')
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            first_name = serializer.data.get('first_name')
            last_name = serializer.data.get('last_name')
            balance = serializer.data.get('balance')
            pin = serializer.data.get('pin')
            if not User.objects.filter(email=email).exists():
                user = User(card_no=card_no, email=email, first_name=first_name,
                            last_name=last_name, balance=balance, pin=pin)
                user.set_password(password)
                user.save()
                return Response({
                    "users": UserSerializer(user).data,
                    "token": AuthToken.objects.create(user)[1] 
                }, status=status.HTTP_201_CREATED)
                # return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        else:
            return Response(UserSerializer(status=status.HTTP_409_CONFLICT))


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = LoginUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        if user.last_login is None :
            user.first_login = True
            user.save()
            
        elif user.first_login:
            user.first_login = False
            user.save()
            
        login(request, user)
        return super().post(request, format=None)

class UserAPI(generics.RetrieveAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

# class LoginAPI(KnoxLoginView):
#     permission_classes = (permissions.AllowAny,)

#     def post(self, request, format=None):
#         serializer = AuthTokenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)
#         return super(LoginAPI, self).post(request, format=None)

# class UserAPI(generics.RetrieveAPIView):
#     permission_classes = [permissions.IsAuthenticated, ]
#     serializer_class = UserSerializer

#     def get_object(self):
#         return self.request.user

class TransactionView(APIView):
    serializer_class = TransactionSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            transfer_account = serializer.data.get('transfer_account')
            transfer_amount = serializer.data.get('transfer_amount')
            notes = serializer.data.get('notes')
            account_no = serializer.data.get('account_no')
            account = User.objects.get(id=account_no)
            transaction = Transactions(transfer_account=transfer_account, transfer_amount=transfer_amount, notes=notes, account_no=account)
            transaction.save()
            return Response(TransactionSerializer(transaction).data, status=status.HTTP_201_CREATED)


# class CustomerViewSet (viewsets.ModelViewSet):
#     queryset = Customers.objects.all().order_by('first_name')
#     serializer_class = RegisterSerializer



