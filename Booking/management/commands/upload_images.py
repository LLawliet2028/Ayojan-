import os
import random
from django.core.management.base import BaseCommand
from Booking.models import Venues  # Replace with your app name
from PIL import Image
from django.core.files import File

class Command(BaseCommand):
    help = 'Randomly upload images to venues'

    def handle(self, *args, **kwargs):
        image_folder = 'D:\\CodeStuff\\Ayojan\\Mock_images'  # Folder where the images are stored
        images = os.listdir(image_folder)  # List all image files in the folder
        venues = Venues.objects.all()

        if not images:
            self.stdout.write(self.style.ERROR('No images found in the image folder.'))
            return

        # Loop through venues and assign a random image to each venue
        for index, venue in enumerate(venues, start=1):
            random_image = random.choice(images)
            image_path = os.path.join(image_folder, random_image)

            # Ensure the image file exists before proceeding
            if not os.path.exists(image_path):
                self.stdout.write(self.style.WARNING(f'Image {random_image} not found. Skipping.'))
                continue

            # Create a new image name based on the venue name and index
            new_image_name = f'{venue.venue_name}_{index}{os.path.splitext(random_image)[1]}'

            # Open the image using Pillow and assign it to the venue
            with open(image_path, 'rb') as img_file:
                venue.image.save(new_image_name, File(img_file), save=True)
            
            # Log the successful upload
            self.stdout.write(self.style.SUCCESS(f'Uploaded {new_image_name} to {venue.venue_name}'))

