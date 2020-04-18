import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'Snippets.settings'

import django
django.setup()

from opl.models import OplOrderDetails
from opl.operations.FulfillmentEligibleSBP import fulfillment_eligible_sbp

def GetPendingProvisioningOrders():
    PendingProvAll=OplOrderDetails.objects.filter(flowStatus='PENDING PROVISIONING')
    return PendingProvAll

def MakeFEReqPayload(i):
    payload={
        'salesOrderNo': i.salesOrderNo,
        'offerName': i.offerName,
        'initialTerm': i.initialTerm,
        'autoRenewalFlag': i.autoRenewalFlag,
        'tfEligible': i.tfEligible,
        'subRefId': i.subRefId,
        'subscriptionId': i.subscriptionId,
        'deliveryMethod': i.deliveryMethod,
        'prov_email': i.prov_email,
        'requestedStartDate': i.requestedStartDate,
        'quantity': i.quantity
    }
    return payload

def FEScheduler(req):
    resp=fulfillment_eligible_sbp(req)
    return resp


if __name__ == "__main__":
    OrdersInFE=GetPendingProvisioningOrders()
    try:
        for i in OrdersInFE:
            reqPayload=MakeFEReqPayload(i)
            FEScheduler(reqPayload)
        print("{'Reserve Status':'SUCCESS'}")
    except Exception as e:
        print("{'Reserve Status':'FAILURE'}")
        print(e)






