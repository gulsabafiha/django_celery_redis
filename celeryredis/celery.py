from __future__ import absolute_import,unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryredis.settings')

app = Celery('celeryredis')

app.conf.enable_utc=False

app.conf.update(timezone='Asia/Dhaka')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

#celery beat modules
app.conf.beat_schedule={
     'send-email-every-hour':{
         'task':'base.task.send_mail_task',
         'schedule':crontab(hour=18,minute=7,day_of_month=19,month_of_year=6),
     }
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')