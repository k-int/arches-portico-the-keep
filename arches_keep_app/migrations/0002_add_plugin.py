from django.db import migrations, models

def add_keep_app_plugin(apps, schema_editor):
    Plugin = apps.get_model("models", "Plugin")

    if not Plugin.objects.filter(pk="eb53e958-9ddf-40a9-8acd-da2b27df8340").exists():
        Plugin.objects.update_or_create(
            pluginid="eb53e958-9ddf-40a9-8acd-da2b27df8340",
            name={"en": "Keep Integration Dashboard"},
            icon="fa fa-link",
            component="views/components/plugins/keep_integration_dashboard",
            componentname="keep_integration_dashboard",
            config={
                "show": True,
                "is_workflow": False,
                "description": {"en": None},
                "i18n_properties": ["description"],
            },
            slug="keep_integration_dashboard",
            sortorder=1,
        )

def remove_keep_app_plugin(apps, schema_editor):
    Plugin = apps.get_model("models", "Plugin")
    keep_integration_plugin = Plugin.objects.get(pk="eb53e958-9ddf-40a9-8acd-da2b27df8340")
    keep_integration_plugin.delete()

class Migration(migrations.Migration):

    dependencies = [
        ("arches_keep_app", "0001_initial")
    ]

    operations = [
        migrations.RunPython(
            add_keep_app_plugin,
            remove_keep_app_plugin,
        ),
    ]