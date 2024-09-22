import json
import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from Booking.models import Venues, Professional, Amenity, ProfessionalReview, Review
from django.shortcuts import get_object_or_404

class Command(BaseCommand):
    help = 'Load mock data into the database'

    def handle(self, *args, **kwargs):
        base_dir = os.path.dirname(__file__)

        # Load the mock data from JSON files
        with open(os.path.join(base_dir, 'venues.json')) as f:
            venues = json.load(f)
        
        with open(os.path.join(base_dir, 'professionals.json')) as f:
            professionals = json.load(f)

        with open(os.path.join(base_dir, 'venue_reviews.json')) as f:
            venue_reviews = json.load(f)
        
        with open(os.path.join(base_dir, 'professional_reviews.json')) as f:
            professional_reviews = json.load(f)

        # Fetch or create users in the database
        user_data = ['om', 'ompushkar', 'Khushi']
        users = {}
        for username in user_data:
            user, created = User.objects.get_or_create(username=username)
            users[username] = user

        # Create amenities and venues
        for venue_data in venues:
            amenities_data = venue_data.pop('amenities')
            
            # Ensure venues are not duplicated by checking the name or another unique field
            venue, created = Venues.objects.get_or_create(venue_name=venue_data['venue_name'], defaults=venue_data)

            # Create or get amenities and associate with the venue
            for amenity_name in amenities_data:
                amenity, _ = Amenity.objects.get_or_create(name=amenity_name)
                venue.amenities.add(amenity)

            venue.save()

        # Create professionals
        for professional_data in professionals:
            # Check if professional already exists by name or another unique field
            Professional.objects.get_or_create(name=professional_data['name'], defaults=professional_data)

        # Create venue reviews
        for review_data in venue_reviews:
            venue = get_object_or_404(Venues, pk=int(review_data['venue_id']))
            user = users.get(review_data['user'])
            
            # Check if review already exists to avoid duplicates
            Review.objects.get_or_create(
                venue=venue,
                user=user,
                defaults={
                    'rating': review_data['rating'],
                    'comment': review_data['comment'],
                    'date_posted': review_data['date_posted']
                }
            )

        # Create professional reviews
        for review_data in professional_reviews:
            professional = get_object_or_404(Professional, pk=int(review_data['professional_id']))
            user = users.get(review_data['user'])
            
            # Check if professional review already exists
            ProfessionalReview.objects.get_or_create(
                professional=professional,
                user=user,
                defaults={
                    'rating': review_data['rating'],
                    'comment': review_data['comment'],
                    'date_posted': review_data['date_posted']
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully loaded mock data'))
