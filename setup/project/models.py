import datetime

from django.db import models

# Create your models here.
# class Users(models.Model):
#     username = models.CharField(max_length=60)
#     password = models.CharField(max_length=60)

class Customers(models.Model):
    id = models.AutoField(primary_key=True, db_column='account_no')
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    pin = models.IntegerField()
    card_no = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=15, decimal_places=3)
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    # user_id = models.ForeignKey(Users, null=True, blank=True, on_delete=models.SET_NULL)

class Transactions(models.Model):
    transfer_account = models.CharField(max_length=20)
    transfer_amount = models.DecimalField(max_digits=15, decimal_places=3)
    notes = models.CharField(max_length=200)
    transfer_date = models.DateField(default=datetime.date.today)

class Customers_Transactions(models.Model):
    account_no = models.ForeignKey(Customers, null=True, blank=True, on_delete=models.CASCADE)
    transaction_id = models.ForeignKey(Transactions, null=True, blank=True, on_delete=models.SET_NULL)




