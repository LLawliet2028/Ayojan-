from django.contrib import admin
from .models import Vendor, Booking, Notification

admin.site.register(Vendor)
admin.site.register(Booking)
admin.site.register(Notification)
