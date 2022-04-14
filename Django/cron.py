from home.models import *

def my_scheduled_job():
    Machine.objects.all().update(record_today=0)