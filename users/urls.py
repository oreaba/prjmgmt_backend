from django.contrib import admin
from django.urls import path
from .views import LoginView


from users.views import home

urlpatterns = [
    path('', home, name='user-home'),
    path('api/login', LoginView.as_view(), name='api-login'),
   
]


# # Custom title for your API documentation
# api_info = openapi.Info(
#     title="Your Custom API Title",
#     default_version='v1',
#     description="Your API description",
#     terms_of_service="https://www.example.com/policies/terms/",
#     contact=openapi.Contact(email="contact@example.com"),
#     license=openapi.License(name="BSD License"),
# )

# schema_view = get_schema_view(
#     api_info,
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )
