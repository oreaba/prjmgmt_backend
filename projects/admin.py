from django.contrib import admin
from projects.models import Project, ProjectPriority, ProjectStatus, ProjectUser
# Register your models here.



# hide the created_by field from the form, and get it automatically from the request.user
class ProjectAdmin(admin.ModelAdmin):
    exclude = ('created_by',)  # Exclude 'created_by' field from the form

    list_display = ['project_id', 'name', 'description', 'manager','start_date', 'end_date', 'status', 'priority', 'created_by', 'created_at', 'updated_at'] # 'get_manager_name', 
    list_select_related = ['status', 'priority', 'manager', 'created_by']

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
admin.site.register(ProjectStatus)
admin.site.register(ProjectUser)


admin.site.site_header = "Project Management"
admin.site.site_title = "Project Management"
admin.site.index_title = "Welcome to Project Management Portal"

