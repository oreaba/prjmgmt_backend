# to replace 'Token' with 'Bearer'
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
# from django.contrib.auth.models import update_last_login

class BearerTokenAuthentication(TokenAuthentication):
    """to replace 'Token' with 'Bearer'"""
    keyword = 'Bearer'

    # def authenticate_credentials(self, key):
    #     model = self.get_model()
    #     try:
    #         token = model.objects.get(key=key)
    #     except model.DoesNotExist:
    #         raise AuthenticationFailed('Invalid token')

    #     if not token.user.is_active:
    #         raise AuthenticationFailed('User inactive or deleted')
    #     print(update_last_login(None, token.user))
    #     print(token.user.last_login)
    #     print(token)
    #     return (token.user, token)
    

from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth.backends import BaseBackend

from django.contrib.auth import get_user_model
class PMUserBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None