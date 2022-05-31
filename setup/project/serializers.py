from rest_framework import serializers
from django.contrib.auth.models import User
from .models import User, Transactions

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'pin', 'card_no', 'balance', 'email', 'password', 'is_active', 'email_verified', 'date_joined')


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'card_no', 'email', 'password', 'pin', 'balance')
        extra_kwargs = {
            'password': {'write_only': True},
            }

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ('transfer_account', 'transfer_amount', 'notes', "account_no")

# class RegisterSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Customers
#         fields = ('id', 'first_name', 'last_name', 'pin', 'card_no', 'balance', 'username', 'password')
#         extra_kwargs = {
#             'pin': {'write_only': True},
#             'password': {'write_only': True},
#         }

# class TransactionSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Transactions
#         fields = ('id',)



# class RegistrationSerializer(serializers.HyperlinkedModelSerializer):
#     confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
#     class Meta:
#         model = Users
#         fields =['card_no', 'pin', 'username', 'password', 'confirm_password']
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }






