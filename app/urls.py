from django.urls import path
from .views import inbox, add_task, toggle_task, delete_task, settings, statistics


urlpatterns = [
    path("inbox", inbox, name="inbox"),
    path('settings/', settings, name='settings'),
    path('statistics/', statistics, name='statistics'),


    path("add_task", add_task, name="add_task"),
    path("toggle_task", toggle_task, name="toggle_task"),
    path("delete_task", delete_task, name="delete_task"),
]
