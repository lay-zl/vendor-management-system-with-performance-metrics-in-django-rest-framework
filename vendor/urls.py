from rest_framework import routers
from .views import *
from django.urls import path
urlpatterns = [
    path('vendors/',VendorDetails.as_view()),
    path('vendors/<int:pk>/',VendorDetails.as_view()),
    path('purchase_orders/',PurchesOrderDetails.as_view()),
    path('purchase_orders/<int:pk>/',PurchesOrderDetails.as_view()),
    path('vendors/<int:pk>/performance/', VendorPerformanceView.as_view(), name='vendor-performance'),
    path('purchase_orders/<int:pk>/acknowledge/', AcknowledgePurchaseOrderView.as_view(), name='acknowledge-purchase-order'),
]