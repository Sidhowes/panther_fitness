# Generated by Django 3.1.3 on 2020-12-20 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0003_auto_20201220_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='membership_type',
            field=models.CharField(choices=[('Beginner', 'beg'), ('Professional', 'pro')], default='Beginner', max_length=40),
        ),
    ]
