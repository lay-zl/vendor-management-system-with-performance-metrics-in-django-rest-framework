from django.db import models
import uuid
# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=225)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.UUIDField(default=uuid.uuid4,unique=True,editable=False)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg=models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

class PurchesOrder(models.Model):
    po_number = models.CharField(max_length=225,unique=True,default=uuid.uuid4)
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE,related_name='purchesorder')
    order_date = models.DateTimeField(auto_now=True)
    delivery_date = models.DateTimeField(blank=True,null=True)
    items = models.JSONField(null=True,blank=True)
    quantity = models.IntegerField()
    status = models.CharField(max_length=10,default='pending',choices=(('pending','pending'),('completed','completed'),('canceled','canceled')))
    quality_rating = models.FloatField(null=True,blank=True)
    issue_date = models.DateTimeField(null=True,blank=True)
    acknowledgment_date = models.DateTimeField(null=True,blank=True)


class HistoricalPerformancesModel(models.Model):
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE,related_name='HistoricalPerformances')
    date = models.DateTimeField()
    on_time_delivery_rate = models.DateTimeField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()