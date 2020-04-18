from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import OplOrderDetails
from .serializers import OplOrderSerializer,ReserveReqSerializer,fulfillmentEligibleSerializer,ProvCompleteStatusSyncSolSerializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from opl.operations import ReserveSubscriptionSol,FulfillmentEligibleSBP
from rest_framework.response import Response



# Create your views here.

@api_view(['POST'])
@csrf_exempt
def reserveSubView(request):
    ser=ReserveReqSerializer(data=request.data)
    if ser.is_valid():
        reserveSubResp = ReserveSubscriptionSol.reserve_subscription_sol(ser.data)
        OplOrderDetails.objects.create(salesOrderNo= reserveSubResp['salesOrderNo'],offerName=reserveSubResp['offerName'],subRefId=reserveSubResp['subRefId'],subscriptionId=reserveSubResp['subscriptionId'])
        return JsonResponse(reserveSubResp,status=201)
    return JsonResponse(ser.errors,status=400)

class ProvCompleteStatusSyncSolView(APIView):
    def post(self,request):
        ser=ProvCompleteStatusSyncSolSerializer(data=request.data)
        if ser.is_valid():
            OplOrderDetails.objects.filter(salesOrderNo=ser.data['salesOrderNo']).update(flowStatus='CLOSED')
            return Response(ser.data,status=200)
        return Response(ser.errors,status=400)

@api_view(['POST'])
@csrf_exempt
def fulfillmentEligibleView(request):
    ser=fulfillmentEligibleSerializer(data=request.data)
    if ser.is_valid():
        feSbpResp=FulfillmentEligibleSBP.fulfillment_eligible_sbp(ser.data)
        return JsonResponse(feSbpResp,status=200)
    return JsonResponse(ser.errors,status=400)


@csrf_exempt
@api_view(['GET','POST'])
def opl_data(request):
    if request.method=='GET':
        oplData=OplOrderDetails.objects.all()
        serializer=OplOrderSerializer(oplData,many=True)
        return JsonResponse(serializer.data,safe=False)

    if request.method=='POST':
        #data=JSONParser.parse(request)
        serializer=OplOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)

