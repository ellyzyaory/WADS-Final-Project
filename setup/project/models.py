import datetime

from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class CustomUserManager(UserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """

        if not email:
            raise ValueError("The given email must be set")

        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        # GlobalUserModel = apps.get_model(
        #     self.model._meta.app_label, self.model._meta.object_name
        # )
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    id = models.AutoField(_("account no"), primary_key=True, db_column='account_no')
    first_name = models.CharField(_("first name"),max_length=60, blank=False)
    last_name = models.CharField(_("last name"),max_length=60, blank=False)
    pin = models.IntegerField(_("pin"))
    card_no = models.CharField(_("card_no"),max_length=20, unique=True)
    balance = models.DecimalField(_("balance"),max_digits=15, decimal_places=3, blank=False)
    email = models.EmailField(_("email address"), blank=False, unique=True)
    username = None
    # password = models.CharField(max_length=60)
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    email_verified = models.BooleanField(
        _('email verified'),
        default=False,
        help_text=_(
            "Designates whether this user's email is verified. "
        ),
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

# Create your models here.
# class Users(models.Model):
#     username = models.CharField(max_length=60)
#     password = models.CharField(max_length=60)

# class Customers(models.Model):
#     id = models.AutoField(primary_key=True, db_column='account_no')
#     first_name = models.CharField(max_length=60)
#     last_name = models.CharField(max_length=60)
#     pin = models.IntegerField()
#     card_no = models.CharField(max_length=20)
#     balance = models.DecimalField(max_digits=15, decimal_places=3)
#     username = models.CharField(max_length=60)
#     password = models.CharField(max_length=60)
#     # user_id = models.ForeignKey(Users, null=True, blank=True, on_delete=models.SET_NULL)

class Transactions(models.Model):
    transfer_account = models.IntegerField(_("transfer account"))
    transfer_amount = models.DecimalField(_("transfer amount"), max_digits=15, decimal_places=3)
    notes = models.CharField(_("notes"), max_length=200)
    transfer_date = models.DateTimeField(_("transfer date"), default=timezone.now)
    account_no = models.ForeignKey(User, on_delete=models.PROTECT)

# class Customers_Transactions(models.Model):
#     account_no = models.ForeignKey(Customers, on_delete=models.SET_NULL)
#     transaction_id = models.ForeignKey(Transactions, on_delete=models.CASCADE)




