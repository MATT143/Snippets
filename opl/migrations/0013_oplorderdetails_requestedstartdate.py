# Generated by Django 2.2.11 on 2020-03-29 12:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('opl', '0012_oplorderdetails_flowstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='oplorderdetails',
            name='requestedStartDate',
            field=models.DateField(default=datetime.datetime(2020, 3, 29, 12, 3, 56, 556071, tzinfo=utc)),
        ),
    ]
