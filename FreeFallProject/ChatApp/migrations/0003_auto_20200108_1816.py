# Generated by Django 2.2.6 on 2020-01-08 16:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChatApp', '0002_auto_20200108_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hike',
            name='creation_datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 8, 18, 16, 23, 291832)),
        ),
    ]
