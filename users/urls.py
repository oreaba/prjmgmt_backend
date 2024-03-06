from django.contrib import admin
from django.urls import path
from .views import LoginView


from users.views import home

urlpatterns = [
    path('', home, name='user-home'),
    path('api/login', LoginView.as_view(), name='api-login'),
   
]
