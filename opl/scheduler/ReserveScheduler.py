import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'Snippets.settings'

import django
django.setup()

from opl.models import OplOrderDetails
from opl.operations.ReserveSubscriptionSol import reserve_subscription_sol

def GetEnteredOrders():
    enteredAll=OplOrderDetails.objects.filter(flowStatus='ENTERED')
    return enteredAll

def MakeReserveSubReqPayload(salesOrderNo,offerName):
    payload={'salesOrderNo':salesOrderNo,'offerName':offerName}
    return payload

def ReserveScheduler(req):
    resp=reserve_subscription_sol(req)
    OplOrderDetails.objects.filter(salesOrderNo=resp['salesOrderNo']).update(subscriptionId=resp['subscriptionId'],subRefId=resp['subRefId'])
    return resp
def UpdateStatus(salesOrderNo):
    OplOrderDetails.objects.filter(salesOrderNo=salesOrderNo).update(flowStatus='PENDING PROVISIONING')
    return True

if __name__ == "__main__":
    OrdersInEntered=GetEnteredOrders()
    try:
        for i in OrdersInEntered:
            reqPayload=MakeReserveSubReqPayload(i.salesOrderNo,i.offerName)
            ReserveScheduler(reqPayload)
            UpdateStatus(i.salesOrderNo)
        print("{'Reserve Status':'SUCCESS'}")
    except Exception as e:
        print("{'Reserve Status':'FAILURE'}")
        print(e)






