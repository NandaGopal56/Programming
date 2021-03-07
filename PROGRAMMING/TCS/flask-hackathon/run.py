from app import app

import os
os.system("service redis_6379 start' ")

'''

from celery import current_app
from celery.bin import worker
from app import celery

celery = current_app._get_current_object()

worker = worker.worker(app=celery)

options = {
    'broker':celery.config['CELERY_BROKER_URL'],
    'loglevel':'INFO',
    'traceback':True
}

worker.run(**options)

'''