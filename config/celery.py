# from __future__ import absolute_import, unicode_literals
# import os
# from celery import Celery
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
# app = Celery(name, broker='amqp://guest:guest@localhost:5672//', backend='rpc://', include=['myapp.tasks'])
#
# # app = Celery(__name__)
#
# app.conf.broker_url = 'amqp://guest:guest@localhost:5672//'
#
#
# # app.conf.broker_url = 'amqp://guest:guest@broker:5672//'
# # Import tasks.py to detect tasks
# app.autodiscover_tasks()



from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Manually set the Django settings module
DJANGO_SETTINGS_MODULE = 'config.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', DJANGO_SETTINGS_MODULE)

# Create a Celery application
app = Celery('config')

# Set the broker URL
app.conf.broker_url = 'amqp://guest:guest@localhost:5672//'

# app.conf.broker_url = 'amqp://guest:guest@rabbitmq3:5672/'

# Load task modules from all registered Django app configs
app.autodiscover_tasks()

# Define a task
@app.task(bind=True)
def my_task(self):
    print('This is my task')