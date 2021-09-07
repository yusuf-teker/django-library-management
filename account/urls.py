from django.urls import path
from account.views import exit

urlpatterns = [
    path('exit', exit, name='exit')
]