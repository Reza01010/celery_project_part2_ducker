from __future__ import absolute_import, unicode_literals
from celery import shared_task

@shared_task
def add(x, y):
    print('\n"-_-"' * 20, x+y, '\n"-_-"' * 20)
    return

@shared_task
def add_(x, y):
    print('\n"-_-"' * 20, x+y, '\n"-_-"' * 20)
    return


