from django.db import migrations
from django.conf import settings


def set_site_domain(apps, schema_editor):
    Site = apps.get_model('sites', 'Site')

    for i in settings.ALLOWED_HOSTS:
        site_id = settings.ALLOWED_HOSTS.index(i) + 1
        Site.objects.create(
            id=site_id,
            domain='localhost:8000' if not site_id - 1 else settings.ALLOWED_HOSTS[site_id],
            name='Vk mailing'
        )


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique')
    ]

    operations = [
        migrations.RunPython(set_site_domain)
    ]
