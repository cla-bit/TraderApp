# Generated by Django 4.1.9 on 2023-06-23 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0008_remove_trade_trading_tra_trader__aaf68e_idx_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=100, null=True, verbose_name='Balance'),
        ),
    ]
