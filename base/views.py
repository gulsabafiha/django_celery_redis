from django.http import HttpResponse
from .task import *
from .helper import *
from django_celery_beat.models import PeriodicTask,CrontabSchedule
import json

def index(request):
    test_func.delay()
    return HttpResponse('<h1>Done</h1>')

def send_mail_all(request):
    send_mail_task.delay()
    return HttpResponse('Sent')

def schedule_mail(request):
    schedule,created=CrontabSchedule.objects.get_or_create(hour=1,minute=24)
    task=PeriodicTask.objects.create(crontab=schedule,name='schedule_mail_task_"+" 3',task='base.task.send_mail_task',) #args=json.dumps(([[2,3]]))
    return HttpResponse('Done')
