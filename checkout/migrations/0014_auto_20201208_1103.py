# Generated by Django 3.1.3 on 2020-12-08 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0013_auto_20201208_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='lineitem_total',
            field=models.DecimalField(decimal_places=2, default=1, editable=False, max_digits=6),
        ),
    ]
