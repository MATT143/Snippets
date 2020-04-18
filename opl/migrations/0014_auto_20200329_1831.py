# Generated by Django 2.2.11 on 2020-03-29 13:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('opl', '0013_oplorderdetails_requestedstartdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='oplorderdetails',
            name='quantity',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='oplorderdetails',
            name='requestedStartDate',
            field=models.DateField(default=datetime.datetime(2020, 3, 29, 13, 1, 57, 739379, tzinfo=utc)),
        ),
    ]
