# Generated by Django 2.0.2 on 2019-11-13 08:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fund', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='current_amount',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 11, 13, 13, 52, 44, 893586)),
        ),
    ]
