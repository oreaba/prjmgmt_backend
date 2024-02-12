from django.contrib import admin
from projects.models import Members, Roles, RoleDuty, Projects, ProjectPriority, ProjectStatus, ProjectMembers
# Register your models here.

admin.site.register(Members)
admin.site.register(Roles)
admin.site.register(RoleDuty)
admin.site.register(Projects)
admin.site.register(ProjectPriority)
admin.site.register(ProjectStatus)
admin.site.register(ProjectMembers)
