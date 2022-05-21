from django.core.mail import send_mail


def send_mail_without_celery():
    send_mail('CELERY WORKED YEAh',
    "CELERY IS COOL",
    "smhassanofficial@gmail.com",
    ["fgulsaba@gmail.com"],
    fail_silently=False)
    return None