# Generated by Django 5.0.6 on 2024-06-14 09:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0008_rename_location_professional_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='professional',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Booking.professional'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='venue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Booking.venues'),
        ),
    ]
