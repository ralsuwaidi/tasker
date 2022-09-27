from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()

class Task(models.Model):
    """
    A general task that can be assigned to a user.
    """

    name = models.CharField(
        _("name"), 
        max_length=150, 
        help_text=_("Name your task"))
    description = models.TextField(
        _("description"), 
        blank=True,
        help_text=_("Describe the task"),
        max_length=1500)
    responsible = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="task_responsible"
    )
    is_completed = models.BooleanField(
        _("completed"),
        default=False,
        help_text=_("Is the task completed?")
    )
    deadline = models.DateField(
        _("Due date"),
        null=True,
        blank=True,
        help_text=_("Example: mm/dd/yyyy")
    )
    is_private: models.BooleanField(
        _("private"),
        default=False,
        help_text=_("Hide the task so only the owner and the assignee can view it")
    )
    
    # auto generated fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # form auto saves current logged in user
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name="task_creator")