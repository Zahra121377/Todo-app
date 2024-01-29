# Create your views here.
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import TaskForm
from .models import Task


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("task_list")


class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("task_list")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("task_list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "The task was deleted successfully.")
        return super().delete(request, *args, **kwargs)
