# Generated by Django 3.0.2 on 2020-02-14 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opl', '0004_auto_20200215_0043'),
    ]

    operations = [
        migrations.AddField(
            model_name='oplorderdetails',
            name='subRefId',
            field=models.CharField(default='Sub53600', max_length=20),
        ),
    ]