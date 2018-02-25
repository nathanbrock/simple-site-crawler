from __future__ import absolute_import
from celery import Celery

app = Celery(
    'celery_tasks',
    broker='amqp://admin:mypass@172.25.0.50:5672',
    backend='rpc://',
    include=['celery_tasks.tasks']
)

