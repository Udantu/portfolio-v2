# Generated by Django 3.1.6 on 2021-06-05 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20210605_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='file',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
