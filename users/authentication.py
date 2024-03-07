# to replace 'Token' with 'Bearer'
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

class BearerTokenAuthentication(TokenAuthentication):
    """to replace 'Token' with 'Bearer'"""
    keyword = 'Bearer'

    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.get(key=key)
        except model.DoesNotExist:
            raise AuthenticationFailed('Invalid token')

        if not token.user.is_active:
            raise AuthenticationFailed('User inactive or deleted')

        return (token.user, token)