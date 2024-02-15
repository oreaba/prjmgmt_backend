from django.db import models

# Create your models here.
from django.db import models

# -------------------------------------------------------------------------------------------------                                 
# Level 1 - ADM Organization                    
# Level 2 - Town Planning Sector                - Portfolio
# Level 3 - Spatial Data Department             - Program
# Level 4 - Spatial Information System Section  - Project
# Level 5 - App Team or DB Team                 - Task
# -------------------------------------------------------------------------------------------------
# on portfolio level
class Organization(models.Model):
    organization_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    name_ar = models.CharField(max_length=100, blank=True, null=True)
# -------------------------------------------------------------------------------------------------

# on program level
class Sector(models.Model):
    sector_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    name_ar = models.CharField(max_length=100, blank=True, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, blank=True, null=True)
# -------------------------------------------------------------------------------------------------

# on project levels
class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    name_ar = models.CharField(max_length=100, blank=True, null=True)
    sector = models.ForeignKey(Sector, on_delete=models.PROTECT, blank=True, null=True)
# -------------------------------------------------------------------------------------------------

class Section(models.Model): 
    section_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    name_ar = models.CharField(max_length=100, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, blank=True, null=True)
# -------------------------------------------------------------------------------------------------

class Team(models.Model): 
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    name_ar = models.CharField(max_length=100, blank=True, null=True)
    section = models.ForeignKey(Section, on_delete=models.PROTECT, blank=True, null=True)
# -------------------------------------------------------------------------------------------------

