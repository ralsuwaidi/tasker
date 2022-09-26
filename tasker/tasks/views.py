from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Task


class IndexView(ListView):
    model = Task


task_list_view = IndexView.as_view()


class ListDetailView(DetailView):
    model = Task
    slug_field = "id"
    slug_url_kwarg = "id"


task_detail_view = ListDetailView.as_view()

