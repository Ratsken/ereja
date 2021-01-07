"""
WSGI config for ereja project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import sys
import os

# Add this line
sys.path.insert(0, os.path.dirname(__file__))

from django.core.wsgi import get_wsgi_application

from dj_static import Cling

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ereja.settings')

application = Cling(get_wsgi_application())