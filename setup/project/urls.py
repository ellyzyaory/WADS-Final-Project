from rest_framework import routers
from django.urls import path, include
from . import views
from knox import views as knox_views

# router = routers.DefaultRouter()
# router.register(r'user', views.UserView.as_view())
# router.register(r'createuser', views.CreateUserView.as_view())
# router.register(r'transactions', views.TransactionView.as_view())

# router.register(r'customers', views.CustomerViewSet)
# router.register(r'users', views.RegistrationViewSet)

urlpatterns = [
    path('', views.home),
    path('payments', views.payments),
    path('profile', views.profile),
    path('login', views.login),
    path('register', views.register),
    path('user', views.UserView.as_view()),
    path('createuser', views.CreateUserView.as_view()),
    path('loginapi', views.LoginAPI.as_view()),
    path('userapi', views.UserAPI.as_view()),
    path('logout', knox_views.LogoutView.as_view()),
    path('transaction', views.TransactionView.as_view()),
    # path('api', include(router.urls)),

]