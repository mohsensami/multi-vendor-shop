from django.urls import path
from . import views


urlpatterns = [
    path('register-user/', views.registerUser, name='register-user'),
    path('register-vendor/', views.registerVendor, name='register-vendor'),
]