from django.urls import path

from tasks.views import TaskCreateView, TaskListView, TaskUpdateView

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("task/add/", TaskCreateView.as_view(), name="task_create"),
    path("task/<int:pk>/edit/", TaskUpdateView.as_view(), name="task_edit"),
]
