from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms


from organizations.models import Team
# Create your models here.
class PMUser(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)

    first_name = models.CharField(max_length=100, blank=True, null=True)
    first_name_ar = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    last_name_ar = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    title_ar = models.CharField(max_length=100, blank=True, null=True)

    extension = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)

    # team = models.ForeignKey(Team, on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        verbose_name        = "User"
        verbose_name_plural = "User"

    def __str__(self):
        return self.username
    

class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=50)
    role_ar = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_required = models.BooleanField(null=False, default = False)

    class Meta:
        verbose_name        = "Role"
        verbose_name_plural = "Role"

    def __str__(self):
        return self.role

class RoleDuty(models.Model):
    duty_id = models.AutoField(primary_key=True)
    duty = models.CharField(max_length=255)
    duty_ar = models.CharField(max_length=255, blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)

    class Meta:
        verbose_name        = "Role Duty"
        verbose_name_plural = "Role Duty"
        

    def __str__(self):
        return self.duty