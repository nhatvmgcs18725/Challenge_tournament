# Generated by Django 3.1.5 on 2021-05-28 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preworktour', '0004_auto_20210528_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverpost',
            name='price',
            field=models.IntegerField(max_length=10000),
        ),
    ]
