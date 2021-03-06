"""
WSGI config for basket_together project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os, sys, site

site.addsitedir("/Users/Jin-TaeWoo/.virtualenvs/projectenv/lib/python3.5/site-packages")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "basket_together.settings.dev")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
