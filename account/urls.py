from django.contrib import auth
from account.views.change_password import change_password
from django.urls import path
from account.views import exit,change_password, registration
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', auth_views.LoginView.as_view(
        template_name = 'pages/login.html'
    ), name='login'),
    path('exit', exit, name='exit'),
    path('change-password', change_password, name='change-password'),
    path("registration", registration, name="registration")
    
]