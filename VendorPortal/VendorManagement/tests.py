from django.test import TestCase
from django.contrib.auth.models import User
from .models import Vendor, Booking

class VendorManagementTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.vendor = Vendor.objects.create(user=self.user, name='Test Vendor', contact_info='123 Test Street')

    def test_create_booking(self):
        booking = Booking.objects.create(vendor=self.vendor, date='2023-01-01', time='12:00:00', description='Test Booking')
        self.assertEqual(booking.description, 'Test Booking')
