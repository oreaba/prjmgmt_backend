from django.db import models
# Create your models here.
from django.db import models
from users.models import User, Role
from organizations.models import Section, Department, Sector


class Portfolio(models.Model):
    portfolio_id = models.AutoField(primary_key=True)

    # Limitation: one portfolio cannot be associated with 2 Sectors.
    # a portfolio can be assigned to only 1 sector
    # a portfolio can have no sector associated with it
    # sector = models.ForeignKey(Sector, on_delete=models.PROTECT, blank=True, null=True) 

    name = models.CharField(max_length=100, blank=True, null=True)
    name_ar = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        verbose_name        = "Portfolio"
        verbose_name_plural = "Portfolio"

    def __str__(self):
        return self.name
# -------------------------------------------------------------------------------------------------
class Program(models.Model):
    program_id = models.AutoField(primary_key=True)
    
    portfolio = models.ForeignKey(Portfolio, on_delete=models.PROTECT, blank=True, null=True)
    # Limitation: one program cannot be associated with 2 departments.
    # a program can be assigned to only 1 department
    # a program can have no department associated with it
    # department = models.ForeignKey(Department, on_delete=models.PROTECT, blank=True, null=True) 

    name = models.CharField(max_length=100, blank=True, null=True)
    name_ar = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        verbose_name        = "Program"
        verbose_name_plural = "Program"

    def __str__(self):
        return self.name
# -------------------------------------------------------------------------------------------------
class Project(models.Model):
    project_id = models.AutoField(primary_key=True)

    program = models.ForeignKey(Program, on_delete=models.PROTECT, blank=True, null=True)
    # Limitation: one project cannot be associated with 2 sections.
    # a project can be assigned to only 1 section
    # a project can have no section associated with it
    # section = models.ForeignKey(Section, on_delete=models.PROTECT, blank=True, null=True)

    name = models.CharField(max_length=100)
    name_ar = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    status = models.ForeignKey('ProjectStatus', on_delete=models.PROTECT)
    priority = models.ForeignKey('ProjectPriority', on_delete=models.PROTECT)
    
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='managed_project')

    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='created_project')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name        = "Project"
        verbose_name_plural = "Project"
    
    def __str__(self):
        return self.name
# -------------------------------------------------------------------------------------------------
class ProjectUser(models.Model):
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)

    class Meta:
        unique_together = (("project", "user", "role"),)
        verbose_name        = "Project User"
        verbose_name_plural = "Project User"

    def __str__(self):
        return f"{self.project} - {self.user} - {self.role}"
# -------------------------------------------------------------------------------------------------
class ProjectStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=50)
    status_ar = models.CharField(max_length=50, blank=True, null=True)
    # color = models.CharField(max_length=7)  # Assuming color code in hexadecimal format
    class Meta:
        verbose_name        = "Project Status"
        verbose_name_plural = "Project Status"

    def __str__(self):
        return self.status
# -------------------------------------------------------------------------------------------------
class ProjectPriority(models.Model):
    priority_id = models.AutoField(primary_key=True)
    priority = models.CharField(max_length=50)
    priority_ar = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=7)  # Assuming color code in hexadecimal format
    class Meta:
        verbose_name        = "Project Priority"
        verbose_name_plural = "Project Priority"

    def __str__(self):
        return self.priority
# -------------------------------------------------------------------------------------------------

    

    