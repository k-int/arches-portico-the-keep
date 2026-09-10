from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("arches_keep_app", "0003_relatededitlogid_fk")]

    def set_is_workflow_false(apps, schema_editor):
        Plugin = apps.get_model("models", "Plugin")

        plugin = Plugin.objects.get(pk="eb53e958-9ddf-40a9-8acd-da2b27df8340")
        plugin.config["is_workflow"] = False
        plugin.save()

    def set_is_workflow_true(apps, schema_editor):
        Plugin = apps.get_model("models", "Plugin")
        plugin = Plugin.objects.get(pk="eb53e958-9ddf-40a9-8acd-da2b27df8340")

        plugin.config["is_workflow"] = True
        plugin.save()

    operations = [
        migrations.RunPython(set_is_workflow_false, set_is_workflow_true),
    ]
