from django.contrib import admin
from django.shortcuts import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import REDIRECT_FIELD_NAME
from apps.login.views import LogUserInView
from .forms import AdminAuthForm


class VKMailingAdminSite(admin.AdminSite):
    site_header = 'VKMailing administration'
    site_title = 'VKMailing site admin'
    login_form = AdminAuthForm

    def login(self, request, extra_context=None):
        if request.method == 'GET' and self.has_permission(request):
            # Already logged-in, redirect to admin index
            index_path = reverse('admin:index', current_app=self.name)
            return HttpResponseRedirect(index_path)

        # Since this module gets imported in the application's root package,
        # it cannot import models from other applications at the module level,
        # and django.contrib.admin.forms eventually imports User.
        from django.contrib.admin.forms import AdminAuthenticationForm
        context = {
            **self.each_context(request),
            'title': 'Log in',
            'app_path': request.get_full_path(),
            'username': request.user.get_username(),
        }
        if (REDIRECT_FIELD_NAME not in request.GET and
                REDIRECT_FIELD_NAME not in request.POST):
            context[REDIRECT_FIELD_NAME] = reverse('admin:index', current_app=self.name)
        context.update(extra_context or {})

        defaults = {
            'extra_context': context,
            'authentication_form': self.login_form,
            'template_name': self.login_template or 'admin/login.html',
        }
        request.current_app = self.name
        return LogUserInView.as_view(**defaults)(request)
    #
    # def logout(self, request, extra_context=None):
    #     pass
