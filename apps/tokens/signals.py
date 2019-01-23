from django.dispatch import Signal


setting_token_cookies_signal = Signal(providing_args=['user', 'refresh_token'])
