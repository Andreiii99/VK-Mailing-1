from django.contrib.admin.forms import AdminAuthenticationForm
from apps.login.forms import LoginForm


class AdminAuthForm(LoginForm, AdminAuthenticationForm):
    pass
