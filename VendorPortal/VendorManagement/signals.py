from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Booking
from django.core.mail import send_mail

@receiver(post_save, sender=Booking)
def send_booking_notification(sender, instance, created, **kwargs):
    if created:
        vendor_email = instance.vendor.user.email
        send_mail(
            'New Booking Received',
            f'You have a new booking on {instance.date}.',
            'from@example.com',
            [vendor_email],
            fail_silently=False,
        )
