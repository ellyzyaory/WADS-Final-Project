from rest_framework import serializers
from django.contrib.auth.models import User
from .models import User, Transactions
from django.contrib.auth import authenticate


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

class User2Serializer(serializers.ModelSerializer):
   
    class Meta:
        model = User
        fields = ('id', 'email', 'first_login' )


class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            if User.objects.filter(email=email).exists():
                user = authenticate(request=self.context.get('request'),
                                    email=email, password=password)
                
            else:
                msg = {'detail': 'Email is not registered.',
                       'register': False}
                raise serializers.ValidationError(msg)

            if not user:
                msg = {
                    'detail': 'Unable to log in with provided credentials.', 'register': True}
                raise serializers.ValidationError(msg, code='authorization')

        else:
            msg = 'Must include "email" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs

# class LoginSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField()
#     password = serializers.CharField()

#     def validate(self, data):
#         user = authenticate(**data)
#         if user and user.is_active:
#             return user
#         raise serializers.ValidationError("Invalid Details.")

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






