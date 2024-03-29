from django.contrib import admin
from projects.models import Project, ProjectPriority, ProjectStatus, ProjectUser, ProjectType
# Register your models here.



# hide the created_by field from the form, and get it automatically from the request.user
class ProjectAdmin(admin.ModelAdmin):
    exclude = ('created_by',)  # Exclude 'created_by' field from the form

    list_display = ['id', 'name', 'description', 'team_lead','start_date', 'end_date', 'status', 'priority', 'created_by', 'created_at', 'updated_at'] # 'get_manager_name', 
    list_select_related = ['status', 'priority', 'team_lead', 'created_by']

    # save the created_by field with the request.user
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # If the object is being created for the first time
            obj.created_by = request.user
        obj.save()

    # def get_manager_name(self, obj):
    #     return obj.manager.get_full_name() if obj.manager else None
    # get_manager_name.short_description = 'Manager'


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectPriority)
admin.site.register(ProjectType)
admin.site.register(ProjectStatus)
admin.site.register(ProjectUser)



from django.contrib.auth.models import Permission, User
admin.site.register(Permission)

from django.contrib.contenttypes.models import ContentType
admin.site.register(ContentType)

from django.contrib.admin.models import LogEntry
admin.site.register(LogEntry)



admin.site.site_header = "Project Management"
admin.site.site_title = "GIS Project Management"
admin.site.index_title = "Admin"
