# Generated by Django 3.1.6 on 2021-05-20 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='author',
            new_name='user',
        ),
    ]
