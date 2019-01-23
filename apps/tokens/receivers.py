from django.dispatch import receiver
from django.apps import apps as dj_apps
from .signals import setting_token_cookies_signal


@receiver(signal=setting_token_cookies_signal)
def refresh_tokens_opirations_receiver(sender, user, refresh_token, **kwargs):
    refresh_tokens_model = dj_apps.get_model('tokens', 'RefreshTokensModel')
    user_tokens = refresh_tokens_model._default_manager.filter(user=user).all()
    user_token = user_tokens.filter(refresh_token=refresh_token).first()

    if not user_token:
        for i in user_tokens.filter(active=True):
            i.update(active=False)

        return refresh_tokens_model._default_manager.create(user=user, active=True, refresh_token=refresh_token)
