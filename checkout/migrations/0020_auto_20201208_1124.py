# Generated by Django 3.1.3 on 2020-12-08 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0019_auto_20201208_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='lineitem_total',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=6),
        ),
    ]
