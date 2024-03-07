# serializers.py
from rest_framework import serializers
from .models import PMUser as User

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'username', 'email', 
                  'firstname', 'firstname_ar', 
                  'lastname', 'lastname_ar', 
                  'title', 'title_ar',
                   'extension', 'mobile',
                  ]  # Add more fields as needed
