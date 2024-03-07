# serializers.py
from rest_framework import serializers
from .models import PMUser as User
from django.utils import timezone


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        # exclude fields
        exclude = ['password',] #, 'user_permissions', 'groups', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined', 'id']
        # ['user_id', 'username', 'email', 
        #           'first_name', 'first_name_ar', 
        #           'last_name', 'lastname_ar', 
        #           'title', 'title_ar',
        #            'extension', 'mobile',
        #           ]  # Add more fields as needed

    def get_last_login(self, obj):
        if obj.last_login is not None:
            local_last_login = obj.last_login.astimezone(timezone.get_current_timezone())
            return local_last_login.strftime("%Y-%m-%dT%H:%M:%S.%f%z")
        return None