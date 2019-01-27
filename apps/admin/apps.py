from django.contrib.admin.apps import AdminConfig


class AdminSiteAdminConfig(AdminConfig):
    default_site = 'apps.admin.admin.VKMailingAdminSite'
