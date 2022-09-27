import django_filters
from tasker.tasks.models import Task

class TaskFilter(django_filters.FilterSet):

    class Meta:
        model = Task
        fields = ['task_stage']
