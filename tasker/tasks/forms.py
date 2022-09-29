from django.forms import ModelForm
from tasker.tasks.models import Task, Update

class TaskCreateForm(ModelForm):
    class Meta:
        model = Task
        exclude = ('created_by',)


class UpdateCreateForm(ModelForm):
    class Meta:
        model = Update
        fields = ['comment', 'file', 'time_spent']