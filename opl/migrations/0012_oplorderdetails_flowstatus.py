# Generated by Django 2.2.11 on 2020-03-28 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opl', '0011_auto_20200328_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='oplorderdetails',
            name='flowStatus',
            field=models.CharField(default='ENTERED', max_length=20),
        ),
    ]
