from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django_filters.views import FilterView

from tasker.tasks.forms import TaskCreateForm, UpdateCreateForm

from .filters import TaskFilter
from .models import Task, Update


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

@login_required
def update_create_view(request, task_id):
    # get the current task instance 
    task = get_object_or_404(Task, pk=task_id)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = UpdateCreateForm(request.POST, request.FILES)
        files = request.FILES.getlist('file')
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            if len(files) <= 1:
                update = form.save(commit=False)
                update.created_by = request.user
                update.task = task
                update.save()
            else:
                # loop over every file and save it manually
                for file in files:
                    print('form', form)
                    update = Update()
                    update.comment = form['comment'].value()
                    update.created_by = request.user
                    update.task = task
                    update.file = file
                    update.save()
            return redirect('tasks:detail', id=task.pk)
    
    else:
        form = UpdateCreateForm()
    return render(request, "tasks/update_form.html", {"form": form, "task_id": task_id})
