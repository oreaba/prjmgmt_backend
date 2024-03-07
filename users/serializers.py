# serializers.py
from rest_framework import serializers
from .models import PMUser as User

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # exclude fields
        exclude = ['password',] #, 'user_permissions', 'groups', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined', 'id']
        # ['user_id', 'username', 'email', 
        #           'first_name', 'first_name_ar', 
        #           'last_name', 'lastname_ar', 
        #           'title', 'title_ar',
        #            'extension', 'mobile',
        #           ]  # Add more fields as needed
