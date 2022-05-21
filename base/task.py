from celery import shared_task
from time import sleep
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from celeryredis import settings


@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        print(i)
    return 'Done'

@shared_task(bind=True)
def send_mail_task(self):
    users=get_user_model().objects.all()
    for user in users:
        mail_subject='Hi celery testing'
        message='If you are good to celery . it will improve'
        to_email=user.email
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=False
        )
    return 'Done'
