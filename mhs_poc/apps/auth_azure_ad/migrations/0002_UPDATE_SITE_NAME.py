# Generated by Django 3.1.5 on 2021-01-15 07:59
from django.conf import settings
from django.db import migrations


def update_site_name(apps, schema_editor):
    SiteModel = apps.get_model("sites", "Site")
    domain = "localhost:8000"

    SiteModel.objects.update_or_create(
        pk=settings.SITE_ID, defaults={"domain": domain, "name": domain}
    )


class Migration(migrations.Migration):

    dependencies = [
        ("sites", "0002_alter_domain_unique"),
        ("auth_azure_ad", "0001_initial"),
    ]
    operations = [migrations.RunPython(update_site_name)]
