from django.urls import path
from . import views


urlpatterns = [
    path('register-user/', views.registerUser, name='register-user'),
    path('register-vendor/', views.registerVendor, name='register-vendor'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('myAccount/', views.myAccount, name='my-account'),
    path('customer-dashboard/', views.customerDashboard, name='customer-dashboard'),
    path('vendor-dashboard/', views.vendorDashboard, name='vendor-dashboard'),

    path('activate/<uidb64>/<token>/', views.activate, name='activate'),

    path('forgot_password/', views.forgot_password, name='forgot-password'),
    path('reset_password_validate/<uidb64>/<token>/', views.reset_password_validate, name='reset_password_validate'),
    path('reset_password/', views.reset_password, name='reset_password'),
]