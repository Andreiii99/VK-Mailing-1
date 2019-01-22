from django.db import migrations
from django.conf import settings


def set_site_domain(apps, schema_editor):
    Site = apps.get_model('sites', 'Site')
    Site.objects.create(
        id=settings.SITE_ID,
        domain='localhost:8000' if not settings.SITE_ID - 1 else settings.ALLOWED_HOSTS[settings.SITE_ID],
        name='Vk mailing'
    )


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique')
    ]

    operations = [
        migrations.RunPython(set_site_domain)
    ]
