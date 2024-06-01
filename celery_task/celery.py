from __future__ import absolute_import,unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_task.settings')
app = Celery('celery_task')
app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Kolkata')
app.config_from_object(settings, namespace='CELERY')

# celery beat settings
app.conf.beat_schedule = {
    'send_periodic_tasks':{
        'task':'test.task.test_func',
        'schedule':crontab(hour=13, minute = 10),
        # 'args':(2,4)

    }
}

app.autodiscover_tasks()

@app.task(bind = True)
def debug_task(self):
    print(f'Request: {self.request!r}')

# import os
# from celery import Celery
# from django.conf import settings

# # Step 1: Check File Location
# print("Checking file location...")
# # Print the current directory to verify where the file is located
# print(f"Current directory: {os.getcwd()}")

# # Step 3: Verify Environment Variables
# print("\nVerifying environment variables...")
# # Print the value of DJANGO_SETTINGS_MODULE
# print(f"DJANGO_SETTINGS_MODULE: {os.environ.get('DJANGO_SETTINGS_MODULE')}")

# # Step 5: Check Celery Worker Logs
# print("\nChecking Celery worker logs...")
# # Add code here to check Celery worker logs for any relevant messages

# # Set the Django settings module for Celery
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_task.settings')

# # Create a Celery instance
# app = Celery('celery_task')

# # Configure Celery to use the correct timezone
# app.conf.enable_utc = False
# app.conf.timezone = 'Asia/Kolkata'

# # Load Celery configuration from Django settings
# app.config_from_object(settings, namespace='CELERY')

# # Autodiscover tasks defined in Django apps
# app.autodiscover_tasks()

# # Define a debug task (optional)
# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')
