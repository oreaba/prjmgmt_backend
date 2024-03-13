"""
URL configuration for prjmgmt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
# from .admin import custom_admin_site
from rest_framework.routers import DefaultRouter
from users import views as user_views
router = DefaultRouter()
# router.register(r'users', user_views.UserViewSet, basename='user')
from django.views.generic import TemplateView


def home(request):
    return JsonResponse({"System":'Project Management'})

urlpatterns = [
    # path('', home, name='prjmgmt-home'),
    path('', TemplateView.as_view(template_name='index.html'), name='home',),  # Serve Angular's index.html

    path('admin/', admin.site.urls),
    #  path('admin/', custom_admin_site.urls),
    
    # internal Applications
    # path('api/', include(router.urls)),
    path('api/users/', include('users.urls')),
    path('api/projects/', include('projects.urls')),
    # path('users/', include('users.urls')),
]
