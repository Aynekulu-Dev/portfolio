"""
WSGI config for portfolio_project project.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

application = get_wsgi_application()

# Automatically run migrations and create superuser on startup
# Safe for Render free tier
from django.core.management import call_command
from django.db.utils import OperationalError

try:
    call_command('migrate', interactive=False)
    call_command('superuser', interactive=False)
except OperationalError:
    # Database might not be ready on first deploy; ignore safely
    pass
except Exception as e:
    print(f"Startup commands failed: {e}")
