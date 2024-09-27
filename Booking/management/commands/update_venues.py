import json
from django.core.management.base import BaseCommand
from Booking.models import Venues

class Command(BaseCommand):
    help = 'Update existing venue data from a single JSON file in the Venues model'

    def handle(self, *args, **kwargs):
        file_path = 'D:\CodeStuff\Ayojan\Ayojan-\Booking\management\commands\\venue_addresses.json'  # Path to the single JSON file containing 98 entries

        # Open the JSON file
        with open(file_path, 'r') as f:
            venues = json.load(f)

        # Loop over the 98 entries and update existing Venue entries by ID
        for idx, venue in enumerate(venues):
            venue_id = idx + 1  # Assuming existing Venue entries have IDs from 1 to 98

            try:
                # Find the existing Venue entry by its primary key (ID)
                venue_obj = Venues.objects.get(pk=venue_id)

                # Parse the address, city, and state from the JSON entry
                parts = venue.split(',')
                address = ', '.join(parts[:-3]).strip()  # Extract address (removing city and state)
                city = parts[-3].strip()  # Extract city
                state = parts[-2].strip()  # Extract state

                # Update the fields
                venue_obj.address = address
                venue_obj.city = city
                venue_obj.state = state

                # Save the updated object
                venue_obj.save()
                self.stdout.write(self.style.SUCCESS(f'Updated Venue ID: {venue_id}'))

            except Venues.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Venue ID: {venue_id} does not exist'))

        self.stdout.write(self.style.SUCCESS('Successfully updated venue data in the database'))
