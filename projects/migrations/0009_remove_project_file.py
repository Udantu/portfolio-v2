# Generated by Django 3.1.6 on 2021-06-05 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_project_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='file',
        ),
    ]
