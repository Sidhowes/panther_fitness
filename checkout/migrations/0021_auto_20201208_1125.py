# Generated by Django 3.1.3 on 2020-12-08 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0020_auto_20201208_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='order',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='checkout.order'),
        ),
    ]