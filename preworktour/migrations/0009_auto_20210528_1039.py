# Generated by Django 3.1.5 on 2021-05-28 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preworktour', '0008_auto_20210528_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverpost',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
