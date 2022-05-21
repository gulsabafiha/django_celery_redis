from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('sendmail/',views.send_mail_all,name='sendmail'),
    path('schedulemail/',views.schedule_mail,name='schedulemail'),
]