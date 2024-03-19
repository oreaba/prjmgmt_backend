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
from users.views import UserViewSet,LoginView

router = DefaultRouter()
router.register(r'users', UserViewSet)
# router.register(r'login', LoginView.as_view(), basename='User')

from django.views.generic import TemplateView

# -------------- for drf api docs
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# -------------------------------------
   

# ---------- api documentation
schema_view = get_schema_view(
    openapi.Info(
        title="ADM Project Management",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="mohammad.oreaba@adm.gov.ae"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

 
def home(request):
    return JsonResponse({"System":'Project Management'})

# ----------------------------------
from tasks.views import HomePageView
urlpatterns = [
    # path('', home, name='prjmgmt-home'),
    
    # path('', TemplateView.as_view(template_name='index.html'), name='home',),  # Serve Angular's index.html
    path('', HomePageView.as_view(), name='home',),  # Serve Angular's index.html

    # path('static', TemplateView.as_view(template_name='index.html'), name='home',),  # Serve Angular's index.html
    # path('static/website/', TemplateView.as_view(template_name='index.html'), name='home2'),  # Serve Angular's index.html

    # DRF includes built-in authentication views that you can access at /api-auth/login/ and /api-auth/logout/.
    # path('api-auth/', include('rest_framework.urls')),  # Include DRF's authentication URLs

    # Djnago Admin Panel
    path('admin/', admin.site.urls),
    #  path('admin/', custom_admin_site.urls),
    

    # -------------------------------------
    # Django DRF Documentation
    path('api/', include(router.urls)),
    # -------------------------------------
    # yasg documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # -------------------------------------

    # internal Applications
    # path('api/', include(router.urls)),
    path('api/users/', include('users.urls')),
    path('api/projects/', include('projects.urls')),
    # path('users/', include('users.urls')),
]

