from django.conf import settings
from django.db import models


class RefreshTokensModel(models.Model):
    refresh_token = models.CharField(max_length=1000, verbose_name='Refresh token')
    active = models.BooleanField(verbose_name='Active')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tokens', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'token_refresh_tokens'
