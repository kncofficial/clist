# Generated by Django 2.1.7 on 2019-11-23 19:13

from django.db import migrations, models


def set_username(apps, schema_editor):
    Coder = apps.get_model('true_coders', 'Coder')
    for c in Coder.objects.all():
        c.save()


class Migration(migrations.Migration):

    dependencies = [
        ('true_coders', '0021_auto_20190818_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='coder',
            name='username',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.RunPython(set_username),
    ]
