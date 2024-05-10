from django.shortcuts import render
from rest_framework import viewsets,routers
from .models import Vendor,PurchesOrder,HistoricalPerformancesModel
from .seralizer import VendorSerializer,PurchesOrderSerializer,HistoricalPerformancesModelSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import *
from django.utils import timezone
from django.db.models import Avg
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status

# Create your views here.

class VendorDetails(APIView):
    def get(self,req,pk=None,format=None):
        id = pk
        if id is not None:
            queryset = Vendor.objects.get(id=id)
            seralizer = VendorSerializer(queryset)
            return Response(seralizer.data)
        else:
            queryset = Vendor.objects.all()
            seralizer = VendorSerializer(queryset,many=True)
            return Response(seralizer.data)

    def post(self,req):
        seralizer=VendorSerializer(data=req.data)
        if seralizer.is_valid():
            seralizer.save()
            return Response({'msg':'Data sucessfully saved ....!'})
        else:
            return Response({'msg':'Smoething Went worrng'},status=status.HTTP_400_BAD_REQUEST)

    def put(self,req,pk,format=None):
        id=pk
        queryset = Vendor.objects.get(id=id)
        seralizer = VendorSerializer(queryset,data=req.data)
        if seralizer.is_valid():
            seralizer.save()
            return Response({'msg':'Data update  sucessfully .....!'})
        else:
            return Response({'msg':'something went wrong'},seralizer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,req,pk=None,format=None):
        id=pk
        queryset = Vendor.objects.get(id=id)
        seralizer=VendorSerializer(queryset,data=req.data,partial=True)
        if seralizer.is_valid():
            seralizer.save()
            return Response({'msg':'Data Update Sucessfully !!'})
        else:
            return Response(seralizer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,req,pk,format=None):
        try:
            queryset = Vendor.objects.get(id=pk)
        except:
            return Response({'msg':'Vendor not found'})
        else:
            queryset.delete()
            return Response({'msg':'Data delete sucessfully....!!'})


'''
function based view

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def vendor_deatills(req,pk=None):
    
    if req.method == 'GET':
        id = pk
        if id is not None:
            queryset = Vendor.objects.get(id=id)
            seralizer = VendorSerializer(queryset)
            return Response(seralizer.data)
        else:
            queryset = Vendor.objects.all()
            seralizer = VendorSerializer(queryset,many=True)
            return Response(seralizer.data)
        
    if req.method == 'POST':
        seralizer=VendorSerializer(data=req.data)
        if seralizer.is_valid():
            seralizer.save()
            return Response({'msg':'Data sucessfully saved ....!'})
        else:
            return Response({'msg':'Smoething Went worrng'},status=status.HTTP_400_BAD_REQUEST)

    if req.method == 'PUT':
        id=pk
        queryset = Vendor.objects.get(id=id)
        seralizer = VendorSerializer(queryset,data=req.data)
        if seralizer.is_valid():
            seralizer.save()
            return Response({'msg':'Data update  sucessfully .....!'})
        else:
            return Response({'msg':'something went wrong'},seralizer.errors,status=status.HTTP_400_BAD_REQUEST)

    if req.method == 'PATCH':
        id=pk

        queryset = Vendor.objects.get(id=id)
        seralizer=VendorSerializer(queryset,data=req.data,partial=True)
        if seralizer.is_valid():
            seralizer.save()
            return Response({'msg':'Data Update Sucessfully !!'})
        else:
            return Response(seralizer.errors,status=status.HTTP_400_BAD_REQUEST)

    if req.method == 'DELETE':
        try:
            queryset = Vendor.objects.get(id=pk)
        except:
            return Response({'msg':'Vendor not found'})
        else:
            queryset.delete()
            return Response({'msg':'Data delete sucessfully....!!'})
'''

class PurchesOrderDetails(APIView):
    def get(self,req,pk=None):

        id=pk
        if pk is not None:
            queryset = PurchesOrder.objects.get(id=id)
            seralizer = PurchesOrderSerializer(queryset)
            return Response(seralizer.data)
        else:
            queryset = PurchesOrder.objects.all()
            seralizer = PurchesOrderSerializer(queryset,many=True)
            return Response(seralizer.data)

    def post(self,req):
        seralizer = PurchesOrderSerializer(req.data)
        if seralizer.is_valid():
            seralizer.save()
            return Response({'msg':'Data save Sucessfully ..... !!'})
        else:
            return Response(seralizer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,req,pk):
        id=pk
        queryset = PurchesOrder.objects.get(id=id)
        seralizer = PurchesOrderSerializer(queryset,data=req.data)
        if seralizer.is_valid():
            seralizer.save()
            return Response({'msg':'Data update Sucessfully ..... !!'},status=status.HTTP_201_CREATED)
        else:
            return Response(seralizer.errors,status=status.HTTP_400_BAD_REQUEST)



    def delete(self,req,pk):
        try:
            queryset = Vendor.objects.get(id=pk)
        except:
            return Response({'msg': 'Order not found'})
        else:
            queryset.delete()
            return Response({'msg': 'Data delete sucessfully....!!'})

class VendorPerformanceView(generics.RetrieveAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({'on_time_delivery_rate': serializer.data['on_time_delivery_rate'],
                 'quality_rating_avg': serializer.data['quality_rating_avg'],
                 'average_response_time': serializer.data['average_response_time'],
                 'fulfillment_rate': serializer.data['fulfillment_rate']})
        # return Response(serializer.data['on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate'])

class AcknowledgePurchaseOrderView(generics.UpdateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = PurchesOrder.objects.all()
    serializer_class = PurchesOrderSerializer

    def create(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.acknowledgment_date = request.data.get('acknowledgment_date')    #timezone.now()
        instance.save()
        response_times = PurchesOrder.objects.filter(vendor=instance.vendor, acknowledgment_date__isnull=False).values_list('acknowledgment_date', 'issue_date')
        average_response_time = sum(abs((ack_date - issue_date).total_seconds()) for ack_date, issue_date in response_times) #/ len(response_times)
        if response_times:
            average_response_time = average_response_time / len(response_times)
        else:
            average_response_time = 0  # Avoid division by zero if there are no response times
        instance.vendor.average_response_time = average_response_time
        instance.vendor.save()
        return Response({'acknowledgment_date': instance.acknowledgment_date})