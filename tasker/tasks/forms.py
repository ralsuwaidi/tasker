from django.forms import ModelForm
from tasker.tasks.models import Task

class TaskCreateForm(ModelForm):
    class Meta:
        model = Task
        exclude = ('created_by',)



