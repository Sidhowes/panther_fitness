# Generated by Django 3.1.3 on 2020-12-27 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20201224_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='has_programme',
        ),
    ]
