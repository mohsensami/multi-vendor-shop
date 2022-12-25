from django.urls import path
from . import views


urlpatterns = [
    path('register-user/', views.registerUser, name='register-user'),
    path('register-vendor/', views.registerVendor, name='register-vendor'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    # path('myAccount/', views.myAccount, name='myAccount'),
]