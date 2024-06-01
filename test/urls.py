from django.urls import path
from test import views


urlpatterns = [
    path('home/',views.home,name="home"),
    path('test/',views.test,name="test"),
    path('schedule_test/',views.schedule_test,name="schedule_test"),
]
