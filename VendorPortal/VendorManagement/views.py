from django.shortcuts import render
from rest_framework import viewsets
from .models import Vendor, Booking, Notification
from .serializers import VendorSerializer, BookingSerializer, NotificationSerializer

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

# Create your views here.
