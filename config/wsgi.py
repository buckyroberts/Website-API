import os

from django.core.wsgi import get_wsgi_application

from config.helpers.environment import SETTINGS_MODULE

os.environ.setdefault('DJANGO_SETTINGS_MODULE', SETTINGS_MODULE)

application = get_wsgi_application()

if os.getenv('SENTRY_DSN'):
    from sentry_sdk.integrations.wsgi import SentryWsgiMiddleware

    application = SentryWsgiMiddleware(application)
