from django.urls import path

from tasks.views import (
    TaskCreateView,
    TaskDeleteView,
    TaskListView,
    TaskUpdateView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("task/add/", TaskCreateView.as_view(), name="task_create"),
    path("task/<int:pk>/edit/", TaskUpdateView.as_view(), name="task_edit"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),
]
