# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from .forms import TaskForm
from .models import Task


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"

    success_url = reverse_lazy("task_list")
    # def form_valid(self, form):
    #     self.object = form.save()

    #     success_message = "Task '{}' was created successfully!".format(
    #         self.object.title
    #     )
    #     return HttpResponse(success_message)


class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("task_list")
