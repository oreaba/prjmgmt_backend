from django.db import models

# Create your models here.
from django.db import models

class Members(models.Model):
    member_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    name_ar = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=20)
    extension = models.CharField(max_length=10, blank=True, null=True)
    title = models.CharField(max_length=100)
    title_ar = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Roles(models.Model):
    role_id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=50)
    role_ar = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.role

class RoleDuty(models.Model):
    duty_id = models.AutoField(primary_key=True)
    duty = models.CharField(max_length=100)
    duty_ar = models.CharField(max_length=100, blank=True, null=True)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)

    def __str__(self):
        return self.duty

class ProjectPriority(models.Model):
    priority_id = models.AutoField(primary_key=True)
    priority = models.CharField(max_length=50)
    priority_ar = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=7)  # Assuming color code in hexadecimal format

    def __str__(self):
        return self.priority

class ProjectStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=50)
    status_ar = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=7)  # Assuming color code in hexadecimal format

    def __str__(self):
        return self.status

class Projects(models.Model):
    project_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    name_ar = models.CharField(max_length=100, blank=True, null=True)
    priority = models.ForeignKey(ProjectPriority, on_delete=models.CASCADE)
    status = models.ForeignKey(ProjectStatus, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ProjectMembers(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    member = models.ForeignKey(Members, on_delete=models.CASCADE)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("project", "member", "role"),)

    def __str__(self):
        return f"{self.project} - {self.member} - {self.role}"
