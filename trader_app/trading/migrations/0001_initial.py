# Generated by Django 4.1.9 on 2023-06-23 14:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('trader', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Trader')),
            ],
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=100, verbose_name='Amount')),
                ('profit_loss', models.DecimalField(decimal_places=2, max_digits=100, verbose_name='Profit/Loss')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('trader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trades', to='trading.trader', verbose_name='Trade')),
            ],
        ),
    ]
