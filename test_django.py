#!/usr/bin/env python
import os
import sys

# Add the project to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fly_starter.settings')

try:
    import django
    django.setup()
    print("✅ Django setup successful!")
    print(f"Django version: {django.get_version()}")
    
    from django.conf import settings
    print(f"DEBUG: {settings.DEBUG}")
    print(f"ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
    print(f"Database: {settings.DATABASES['default']['ENGINE']}")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()