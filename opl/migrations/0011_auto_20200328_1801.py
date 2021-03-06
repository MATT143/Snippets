# Generated by Django 2.2.11 on 2020-03-28 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opl', '0010_auto_20200316_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='oplorderdetails',
            name='deliveryMethod',
            field=models.CharField(default='NA', max_length=10),
        ),
        migrations.AddField(
            model_name='oplorderdetails',
            name='prov_email',
            field=models.EmailField(default='NA', max_length=254),
        ),
        migrations.AlterField(
            model_name='oplorderdetails',
            name='subRefId',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
