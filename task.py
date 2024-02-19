# from workers import celery_app
from celery import shared_task
import time

# @celery_app.task
# def sum(a,b):
#     time.sleep(60)
#     return a+b

@shared_task(ignore_result=False)
def sum(a,b):
    time.sleep(60)
    return a+b