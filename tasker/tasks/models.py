from django.db import models
from django.utils.translation import gettext_lazy as _

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
        null=True
    )
    is_completed = models.BooleanField(
        _("Is the task completed?"),
        default=False
    )
    deadline = models.DateField(
        _("Due date"),
        null=True,
        blank=True,
        help_text=_("Example: mm/dd/yyyy")
    )
    
    # auto generated fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)