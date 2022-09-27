from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django_filters.views import FilterView
from .filters import TaskFilter
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from tasker.tasks.forms import TaskCreateForm

from .models import Task


class TaskListView(FilterView):
    model = Task
    context_object_name = 'task_list'
    template_name = 'tasks/task_list.html'
    filterset_class = TaskFilter


task_list_view = TaskListView.as_view()


class TaskDetailView(DetailView):
    model = Task
    slug_field = "id"
    slug_url_kwarg = "id"


task_detail_view = TaskDetailView.as_view()


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskCreateForm

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return reverse('tasks:list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


task_create_view = TaskCreateView.as_view()


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskCreateForm
    slug_field = "id"
    slug_url_kwarg = "id"

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return reverse('tasks:list')


task_update_view = TaskUpdateView.as_view()

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    slug_field = "id"
    slug_url_kwarg = "id"

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return reverse('tasks:list')


task_delete_view = TaskDeleteView.as_view()
