import os
from celery import Celery
from django.conf import settings

# os.environ.setdefault('DJANGO_SETTINGS_MODULES', 'my_publisher.settings')
os.environ['DJANGO_SETTINGS_MODULE'] = 'my_publisher.settings'

app = Celery('my_publisher')
app.config_from_object('django.conf:settings')

app.autodiscover_tasks()