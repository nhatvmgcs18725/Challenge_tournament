# Generated by Django 3.1.5 on 2021-05-28 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preworktour', '0005_auto_20210528_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverpost',
            name='price',
            field=models.IntegerField(),
        ),
    ]
