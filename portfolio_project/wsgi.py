"""
WSGI config for portfolio_project project.
"""

import os
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

# Run migrations automatically on startup
try:
    call_command('migrate', interactive=False)
except Exception as e:
    print(f"Migration failed: {e}")

application = get_wsgi_application()





"""
WSGI config for portfolio_project project.
"""

import os
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

# Run migrations and create superuser on startup
try:
    call_command('migrate', interactive=False)
    call_command('superuser', interactive=False)
except Exception as e:
    print(f"Startup commands failed: {e}")

application = get_wsgi_application()