# Generated by Django 3.1.6 on 2021-06-06 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_project_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='urlType',
            new_name='srcType',
        ),
        migrations.RemoveField(
            model_name='project',
            name='file',
        ),
    ]
