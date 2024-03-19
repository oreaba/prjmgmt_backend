from django.contrib import admin
from .models import Role, RoleDuty
from django.contrib.auth.models import User
from users.models import PMUser #as User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from django.forms import inlineformset_factory
from users.forms import RoleDutyForm

# Register your models here.
class PMUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = PMUser

class PMUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = PMUser

class PMUserAdmin(UserAdmin):
    add_form = PMUserCreationForm
    form = PMUserChangeForm
    model = PMUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'last_login']

    fieldsets = (
        (None, {'fields': ('username', 'password' )}),
        # ('Change Password', {'fields': ('password1','password2')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Additional Info', {'fields': ('first_name_ar', 'last_name_ar', 'title', 'title_ar', 'extension', 'mobile')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
                                        # 'password2'
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_superuser', 'is_active',  
                       'groups', 'user_permissions', 'first_name', 'last_name', 'first_name_ar', 'last_name_ar',
                        'title', 'title_ar', 'extension', 'mobile',),
        }),
    )

   
admin.site.register(PMUser, PMUserAdmin)    # without adding PMUserAdmin, it will store plain password and it will not show the additional fields in the admin panel

# admin.site.register(Role)
# admin.site.register(RoleDuty)


# RoleDutyFormSet = inlineformset_factory(Role, RoleDuty, form=RoleDutyForm, extra=1)
class RoleDutyInline(admin.TabularInline):
    model = RoleDuty
    # formset = RoleDutyFormSet

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    inlines = [RoleDutyInline]