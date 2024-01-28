from django.urls import path

from tasks.views import TaskCreateView, TaskListView

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("new_task/", TaskCreateView.as_view(), name="new_task"),
]
