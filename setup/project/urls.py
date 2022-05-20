from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('payments', views.payments),
    path('profile', views.profile),

    path('camera', views.camera, name='camera'),
    path('video_stream', views.video_stream, name='video_stream'),

    # path('/sign-up', views.signup, name='signup'),
    # path('/login', views.login, name='login'),

]