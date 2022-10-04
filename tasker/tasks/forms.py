from django import forms
from tasker.tasks.models import Task, Update

class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ('created_by',)


class UpdateCreateForm(forms.ModelForm):
    class Meta:
        model = Update
        fields = ['comment', 'file', 'time_spent']
        widgets = {
            'file': forms.ClearableFileInput(attrs={'multiple': True}),
        }

