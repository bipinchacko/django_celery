from django.shortcuts import render
from django.http import HttpResponse
from .task import test_func
from django_celery_beat.models import PeriodicTask,CrontabSchedule
import json

# Create your views here.
def home(request):
    # return render(request,'longprofile/home.html')
    return HttpResponse("Hello, world bipin!")
def test(request):
    test_func.delay()
    return HttpResponse("Done")
def schedule_test(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour = 1,minute = 10)
    task = PeriodicTask.objects.create(crontab = schedule, task= 'task.test_func', name = "ttt2"+"1", args = json.dumps((2,3)))
    return HttpResponse("Okay")