# Generated by Django 4.1.9 on 2023-06-23 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0003_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]