from django.conf import settings
from django.apps import apps as dj_apps
from django.utils import timezone
from jwt import encode, decode
from .settings import TOKEN_OPTIONS
from .signals import setting_token_cookies_signal
import datetime


def get_token_pair(payload={}, algorithm=TOKEN_OPTIONS['ALGORITHM']):
    payload['exp'] = TOKEN_OPTIONS['ACCESS_TOKEN_EXPIRATION']
    access_token = encode(payload=payload, key=settings.SECRET_KEY, algorithm=algorithm).decode('utf-8')

    refresh_token_payload = {'exp': TOKEN_OPTIONS['REFRESH_TOKEN_EXPIRATION'], 'access_token': access_token}
    refresh_token = encode(payload=refresh_token_payload, key=settings.SECRET_KEY, algorithm=algorithm).decode('utf-8')
    return {'access_token': access_token, 'refresh_token': refresh_token}


def decode_token(token, algorithm='HS256'):
    return decode(token, key=settings.SECRET_KEY, algorithms=[algorithm])


def set_token_cookies(response, user, access_token, refresh_token):
    refresh_tokens_model = dj_apps.get_model('tokens', 'RefreshTokensModel')
    setting_token_cookies_signal.send(sender=refresh_tokens_model, user=user, refresh_token=refresh_token)

    expiration_time = timezone.localtime(timezone.now()) + datetime.timedelta(weeks=24)
    response.set_cookie(key='access_token', value=access_token, expires=expiration_time)
    response.set_cookie(key='refresh_token', value=refresh_token, expires=expiration_time)
    return response
