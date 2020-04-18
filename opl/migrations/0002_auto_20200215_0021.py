# Generated by Django 3.0.2 on 2020-02-14 18:51
from __future__ import unicode_literals
from django.db import migrations


def create_initial_orders(apps, schema_editor):
    OplOrderDetails = apps.get_model('opl', 'OplOrderDetails')
    OplOrderDetails(webOrderId='order1', Offer='A-WX-NAMED-USER', initialTerm=12,autoRenewalFlag=False).save()
    OplOrderDetails(webOrderId='order2', Offer='A-WX-ACTIVE-USER', initialTerm=12, autoRenewalFlag=True).save()
    OplOrderDetails(webOrderId='order3', Offer='A-WX-EMP-COUNT', initialTerm=12, autoRenewalFlag=False).save()
    OplOrderDetails(webOrderId='order4', Offer='A-SPK-NAMED-USER', initialTerm=12, autoRenewalFlag=False).save()
    OplOrderDetails(webOrderId='order5', Offer='A-SPK-ACTIVE-USER', initialTerm=12, autoRenewalFlag=False).save()
    OplOrderDetails(webOrderId='order6', Offer='ELA2-M', initialTerm=12, autoRenewalFlag=False).save()


class Migration(migrations.Migration):

    dependencies = [
        ('opl', '0001_initial'),
    ]

    operations = [migrations.RunPython(create_initial_orders)
    ]
