from rest_framework import serializers
from .models import Project, ProjectStatus, ProjectPriority
from users.models import PMUser as User

class ProjectStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectStatus
        fields = '__all__'# ['status_field_1', 'status_field_2', ...]  # Include the fields you want to serialize for ProjectStatus

class ProjectPrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPriority
        fields = '__all__'# ['priority_field_1', 'priority_field_2', ...]

class ProjectUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'extension', 'mobile'] #['team_lead_field_1', 'team_lead_field_2', ...]

class ProjectSerializer(serializers.ModelSerializer):
    status = ProjectStatusSerializer()  # Use ProjectStatusSerializer to include status details
    priority = ProjectPrioritySerializer()
    team_lead = ProjectUserSerializer()
    created_by = ProjectUserSerializer()
    progress = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'  # Serialize all fields of the Project model

    def get_progress(self, obj):
        # Implement your logic to calculate progress here
        return obj.get_progress()