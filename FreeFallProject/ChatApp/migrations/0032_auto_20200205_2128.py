# Generated by Django 2.2.6 on 2020-02-05 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChatApp', '0031_auto_20200205_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hike',
            name='creation_datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
