import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'planB_backend.settings.production')

application = get_wsgi_application()
