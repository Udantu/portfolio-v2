# Generated by Django 3.1.6 on 2021-06-05 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_remove_project_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='path',
            field=models.TextField(default=''),
        ),
    ]
