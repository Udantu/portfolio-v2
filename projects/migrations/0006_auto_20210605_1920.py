# Generated by Django 3.1.6 on 2021-06-05 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20210605_1919'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='path_file',
            new_name='path',
        ),
    ]
