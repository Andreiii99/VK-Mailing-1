from django.contrib.auth import get_user_model
from apps.tokens.utils import decode_token
from jwt.exceptions import ExpiredSignatureError


class TokenAuthBackend:
    def authenticate(self, request, access_token=None):
        if access_token:
            user_model = get_user_model()

            try:
                credentials = decode_token(access_token)
            except ExpiredSignatureError:
                raise ExpiredSignatureError
            except:
                return None

            user = user_model._default_manager.filter(
                username=credentials['username'],
                password=credentials['password'],
                email=credentials['email']
            ).first()
            return user
        return None

    def get_user(self, user_id):
        user_model = get_user_model()

        try:
            return user_model._default_manager.get(pk=user_id)
        except user_model.DoesNotExist:
            return None
