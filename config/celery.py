from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery(__name__)

app.conf.broker_url = 'amqp://guest:guest@localhost:5672//'

# Import tasks.py to detect tasks
app.autodiscover_tasks()