from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task


class TaskListView(ListView):
    model = Task


task_list_view = TaskListView.as_view()


class TaskDetailView(DetailView):
    model = Task
    slug_field = "id"
    slug_url_kwarg = "id"


task_detail_view = TaskDetailView.as_view()


class TaskCreateView(CreateView, LoginRequiredMixin):
    model = Task
    fields = '__all__'

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return reverse('tasks:list')


task_create_view = TaskCreateView.as_view()


class TaskUpdateView(UpdateView, LoginRequiredMixin):
    model = Task
    fields = '__all__'
    slug_field = "id"
    slug_url_kwarg = "id"

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return reverse('tasks:list')


task_update_view = TaskUpdateView.as_view()

class TaskDeleteView(DeleteView, LoginRequiredMixin):
    model = Task
    slug_field = "id"
    slug_url_kwarg = "id"

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return reverse('tasks:list')


task_delete_view = TaskDeleteView.as_view()
