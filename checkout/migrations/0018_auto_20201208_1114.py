# Generated by Django 3.1.3 on 2020-12-08 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0017_auto_20201208_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='lineitem_total',
            field=models.IntegerField(default=0),
        ),
    ]
