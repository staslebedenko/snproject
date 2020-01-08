# Generated by Django 2.2.6 on 2020-01-08 20:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChatApp', '0004_auto_20200108_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='visible_for',
            field=models.CharField(choices=[('noone', 'noone'), ('friends', 'friends'), ('all', 'all')], default='all', max_length=10),
        ),
        migrations.AlterField(
            model_name='hike',
            name='creation_datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 8, 22, 31, 3, 888201)),
        ),
    ]
