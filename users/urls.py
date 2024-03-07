from django.contrib import admin
from django.urls import path
from .views import LoginView
from rest_framework.authtoken import views

from users.views import home
from users.views import UserProfileAPIView

urlpatterns = [
    path('', home, name='user-home'),

    # Default Djnago authentication
    # path('api/login', LoginView.as_view(), name='api-login'),         # we just added token there - not needed for Default Django Authentication

    # Default DRF authentication
    path('api/token', views.obtain_auth_token, name='auth-token'),     # only drf token
    path('api/login', LoginView.as_view(), name='login'),                       # drf token with custom fields
    path('api/profile', UserProfileAPIView.as_view(), name='user-me'),
    

]
