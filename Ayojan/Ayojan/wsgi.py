import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the project directory to the Python path
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_dir)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ayojan.settings')

# Configure Django
import django
django.setup()

# Wrap the WSGI application in a try-except block for better error reporting
try:
    application = get_wsgi_application()
except Exception as e:
    print(f"Error loading the application: {e}", file=sys.stderr)
    raise

# Add debugging information
from django.conf import settings
print(f"DEBUG: {settings.DEBUG}", file=sys.stderr)
print(f"ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}", file=sys.stderr)
print(f"INSTALLED_APPS: {settings.INSTALLED_APPS}", file=sys.stderr)
print(f"MIDDLEWARE: {settings.MIDDLEWARE}", file=sys.stderr)
print(f"ROOT_URLCONF: {settings.ROOT_URLCONF}", file=sys.stderr)
print(f"WSGI_APPLICATION: {settings.WSGI_APPLICATION}", file=sys.stderr)
print(f"DATABASES: {settings.DATABASES}", file=sys.stderr)
print(f"STATIC_ROOT: {settings.STATIC_ROOT}", file=sys.stderr)
print(f"MEDIA_ROOT: {settings.MEDIA_ROOT}", file=sys.stderr)
