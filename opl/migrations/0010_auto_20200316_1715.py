# Generated by Django 2.2.11 on 2020-03-16 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opl', '0009_auto_20200316_1703'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oplorderdetails',
            old_name='offer',
            new_name='offerName',
        ),
        migrations.RenameField(
            model_name='oplorderdetails',
            old_name='webOrderId',
            new_name='salesOrderNo',
        ),
    ]
