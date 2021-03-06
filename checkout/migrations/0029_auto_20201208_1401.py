# Generated by Django 3.1.3 on 2020-12-08 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0028_auto_20201208_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='orderlineitem',
            name='lineitem_total',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=6),
        ),
    ]
