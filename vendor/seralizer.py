from rest_framework import serializers
from .models import Vendor,PurchesOrder,HistoricalPerformancesModel


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields='__all__'

class PurchesOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchesOrder
        fields  = '__all__'

class HistoricalPerformancesModelSerializer(serializers.ModelSerializer):
    class Meta:
        moodel = HistoricalPerformancesModel
        fields = '__all__'

