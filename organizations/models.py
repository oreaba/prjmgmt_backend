from django.db import models

# Create your models here.
from django.db import models

# -------------------------------------------------------------------------------------------------                                 
# level 1 - ADM Organization                    
# level 2 - Town Planning Sector                - Portfolio
# Level 3 - Spatial Data Department             - Program
# Level 4 - Spatial Information System Section  - Project
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
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT)
# -------------------------------------------------------------------------------------------------

# on project levels
class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    name_ar = models.CharField(max_length=100, blank=True, null=True)
    sector = models.ForeignKey(Sector, on_delete=models.PROTECT)
# -------------------------------------------------------------------------------------------------

class Section(models.Model): 
    section_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    name_ar = models.CharField(max_length=100, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)#, blank=True, null=True))
# -------------------------------------------------------------------------------------------------

