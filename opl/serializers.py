from rest_framework import serializers
from .models import OplOrderDetails
from opl.requestTemplates.OplReserveSubRequest import reserveSubRequest
from opl.requestTemplates.FErequest import fulfillmentEligibleRequest
from opl.requestTemplates.ProvCompleteStausReq import ProvCompleteStausReq

class OplOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=OplOrderDetails
        exclude=['subRefId','subscriptionId']



class ReserveReqSerializer(serializers.Serializer):
    salesOrderNo=serializers.CharField(max_length=20)
    offerName=serializers.CharField(max_length=50)
    def create(self, validated_data):
        return reserveSubRequest(validated_data)

class fulfillmentEligibleSerializer(serializers.Serializer):
    salesOrderNo=serializers.CharField(max_length=20)
    offerName = serializers.CharField(max_length=20)
    initialTerm = serializers.IntegerField()
    autoRenewalFlag = serializers.BooleanField()
    tfEligible = serializers.BooleanField()
    subRefId = serializers.CharField(max_length=20)
    subscriptionId = serializers.CharField(max_length=20)

    def create(self, validated_data):
        return fulfillmentEligibleRequest(validated_data)

class ProvCompleteStatusSyncSolSerializer(serializers.Serializer):
    salesOrderNo=serializers.CharField(max_length=20)
    flowStatus=serializers.CharField(max_length=20)

    def create(self, validated_data):
        return ProvCompleteStausReq(validated_data)







