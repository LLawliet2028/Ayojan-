# Generated by Django 5.0.6 on 2024-06-05 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0002_alter_amenity_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venues',
            name='amenities',
            field=models.ManyToManyField(null=True, to='Booking.amenity'),
        ),
    ]
