from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'customers', views.CustomerViewSet)
# router.register(r'users', views.RegistrationViewSet)

urlpatterns = [
    path('', views.home),
    path('payments', views.payments),
    path('profile', views.profile),
    path('login', views.login),
    path('register', views.register),
    path('api', include(router.urls)),

]