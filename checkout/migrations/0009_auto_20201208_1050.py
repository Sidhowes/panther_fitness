# Generated by Django 3.1.3 on 2020-12-08 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20201130_1141'),
        ('checkout', '0008_auto_20201208_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='lineitem_total',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=6),
        ),
        migrations.AlterField(
            model_name='orderlineitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]
