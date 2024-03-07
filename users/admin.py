from django.contrib import admin
from .models import Role, RoleDuty
from django.contrib.auth.models import User
from users.models import PMUser as User

# Register your models here.

admin.site.register(User)
admin.site.register(Role)
admin.site.register(RoleDuty)