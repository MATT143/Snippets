from django.db import models
from django.utils.timezone import now

# Create your models here.

class OplOrderDetails(models.Model):
    salesOrderNo=models.CharField(max_length=20)
    offerName=models.CharField(max_length=20)
    initialTerm=models.IntegerField()
    autoRenewalFlag=models.BooleanField()
    tfEligible=models.BooleanField()
    subRefId=models.CharField(max_length=20,default=None)
    subscriptionId=models.CharField(max_length=20,default=None)
    deliveryMethod=models.CharField(max_length=10,default='NA')
    prov_email=models.EmailField(default='NA')
    flowStatus=models.CharField(max_length=20,default='ENTERED')
    requestedStartDate=models.DateField(default=now())
    quantity=models.IntegerField(default=100)

    def __str__(self):
        return self.salesOrderNo





