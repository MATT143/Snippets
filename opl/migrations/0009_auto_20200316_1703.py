# Generated by Django 2.2.11 on 2020-03-16 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opl', '0008_auto_20200305_1559'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oplorderdetails',
            old_name='Offer',
            new_name='offer',
        ),
    ]