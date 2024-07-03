# VendorManagement/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from .models import Vendor, Booking, Notification
from .serializers import VendorSerializer, BookingSerializer, NotificationSerializer
from django.http import JsonResponse
from django.db.models import Count
import datetime

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        user.save()
        login(request, user)
        return redirect('dashboard')
    return render(request, 'vendormanagement/signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'vendormanagement/login.html')

@login_required
def dashboard(request):
    current_user = request.user
    vendor = Vendor.objects.get(user=current_user)
    bookings = Booking.objects.filter(vendor=vendor)
    return render(request, 'vendormanagement/dashboard.html', {'bookings': bookings})

@login_required
def profile(request):
    current_user = request.user
    vendor = Vendor.objects.get(user=current_user)
    if request.method == 'POST':
        vendor.name = request.POST['name']
        vendor.email = request.POST['email']
        vendor.phone = request.POST['phone']
        vendor.address = request.POST['address']
        vendor.save()
        return redirect('profile')
    return render(request, 'vendormanagement/profile.html', {'vendor': vendor})

@login_required
def booking_detail(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'vendormanagement/booking_detail.html', {'booking': booking})

@login_required
def analytics(request):
    current_user = request.user
    vendor = Vendor.objects.get(user=current_user)
    bookings = Booking.objects.filter(vendor=vendor, date__month=datetime.datetime.now().month)
    booking_count = bookings.count()
    return render(request, 'vendormanagement/analytics.html', {'booking_count': booking_count})

def notifications(request):
    current_user = request.user
    vendor = Vendor.objects.get(user=current_user)
    notifications = Notification.objects.filter(vendor=vendor)
    return render(request, 'vendormanagement/notifications.html', {'notifications': notifications})
