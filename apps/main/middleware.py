from django.contrib.auth import authenticate
from django.contrib.auth.models import AnonymousUser
from django.apps import apps as dj_apps
from jwt.exceptions import ExpiredSignatureError
from apps.tokens.utils import set_token_cookies, get_token_pair


class TokenAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if hasattr(request, 'reset_tokens'):
            refresh_tokens_model = dj_apps.get_model('tokens', 'RefreshTokensModel')
            ref_token_obj = refresh_tokens_model._default_manager.filter(
                refresh_token=request.COOKIES.get('refresh_token'),
                active=True
            ).first()

            if ref_token_obj:
                user = ref_token_obj.user
                payload = {
                    'username': user.username,
                    'password': user.password,
                    'email': user.email
                }
                token_pair = get_token_pair(payload=payload)
                response = set_token_cookies(
                    response,
                    ref_token_obj.user,
                    token_pair['access_token'],
                    token_pair['refresh_token']
                )
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        access_token = request.COOKIES.get('access_token')
        user = None

        if access_token:
            try:
                user = authenticate(request, access_token=access_token)
            except ExpiredSignatureError:
                request.reset_tokens = True

        request.user = user or AnonymousUser()
