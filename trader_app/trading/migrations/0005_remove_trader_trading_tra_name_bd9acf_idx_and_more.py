# Generated by Django 4.1.9 on 2023-06-23 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0004_delete_customuser'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='trader',
            name='trading_tra_name_bd9acf_idx',
        ),
        migrations.RemoveField(
            model_name='trader',
            name='name',
        ),
    ]
