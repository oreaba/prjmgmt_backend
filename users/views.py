from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse



def home(request):
    return JsonResponse({"app":'user'})


# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

from .serializers import LoginSerializer
from users.models import PMUser as User

from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from users.authentication import BearerTokenAuthentication # to use 'Bearer' keyword instead of 'Token'

from django.utils import timezone
from django.contrib.auth.models import update_last_login

from .serializers import UserProfileSerializer
# we use this login view to authenticate user Django's default
# Added for DRF: create and return token for authenticated user

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            # last_login = None
            try:
                # Attempt to retrieve the user object using the provided username
                user = User.objects.get(username=username)
                # Now you can access the last_login attribute of the user
                last_login = user.last_login
            except User.DoesNotExist:
                return None
            user = authenticate(username=username, password=password)
            
            
            # print(type(user))
            if user is not None:
                # User authenticated
                token, created = Token.objects.get_or_create(user=user)     # create token - drf
                # user_data = {
                #     'user_id': user.user_id,
                #     'username': user.username,
                #     'email': user.email,
                #     'token': token.key,
                #     # Add more fields as needed
                # }

                user_profile = User.objects.get(user_id=user.user_id)
                serializer = UserProfileSerializer(user_profile)
                user_data = serializer.data
                # return Response(serializer.data)
                if last_login:
                    user_data['last_login'] = last_login.astimezone(timezone.get_current_timezone())
                # return local_last_login.strftime("%Y-%m-%dT%H:%M:%S.%f%z")

                update_last_login(None, token.user)
                return Response({'detail': 'Login successful', 
                                 'token': token.key,
                                 'user': user_data
                                 }, status=status.HTTP_200_OK)
            else:
                # Authentication failed
                return Response({'detail': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            # Invalid serializer data
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class UserProfileAPIView(APIView):
    # authentication_classes = [TokenAuthentication] # uses Authorization Token 'string'
    authentication_classes = [BearerTokenAuthentication] # uses Authorization Bearer 'string'
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user_profile = User.objects.get(user_id=request.user.user_id)
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data)
