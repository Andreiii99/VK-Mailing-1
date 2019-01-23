from django.utils import timezone
import datetime


TOKEN_OPTIONS = {
    'REFRESH_TOKEN_EXPIRATION': timezone.localtime(timezone.now()) + datetime.timedelta(weeks=4),
    'ACCESS_TOKEN_EXPIRATION': timezone.localtime(timezone.now()) + datetime.timedelta(weeks=1),
    'ALGORITHM': 'HS256'
}
