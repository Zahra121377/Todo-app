from django.urls import path

from tasks.views import TaskCreateView

urlpatterns = [
    path("new_task/", TaskCreateView.as_view(), name="new_task"),
]
