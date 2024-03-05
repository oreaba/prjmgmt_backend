from django.contrib import admin
from projects.models import Project, ProjectPriority, ProjectStatus, ProjectUser
# Register your models here.



admin.site.register(Project)
admin.site.register(ProjectPriority)
admin.site.register(ProjectStatus)
admin.site.register(ProjectUser)


admin.site.site_header = "Project Management"
admin.site.site_title = "Project Management"
admin.site.index_title = "Welcome to Project Management Portal"

