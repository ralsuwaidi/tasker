from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError



class Task(models.Model):
    """
    A general task that can be assigned to a user.
    """

    NEW = 'NW'
    QUE = 'QU'
    PROGRESS = 'PR'
    REVIEW = 'RE'
    COMPLETED = 'CO'
    TASK_STAGE = [
        (NEW, 'New'),
        (QUE, 'In Que'),
        (PROGRESS, 'In Progress'),
        (REVIEW, 'Under Review'),
        (COMPLETED, 'Completed'),
    ]

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
        related_name="task_responsible")
    is_completed = models.BooleanField(
        _("completed"),
        default=False,
        help_text=_("Is the task completed?"))
    is_private = models.BooleanField(
        _("private"),
        default=False,
        help_text=_("Hide the task so only the owner and the assignee can view it"))
    deadline = models.DateField(
        _("Due date"),
        null=True,
        blank=True,
        help_text=_("Example: mm/dd/yyyy"))
    task_stage = models.CharField(
        max_length=2,
        choices=TASK_STAGE,
        default=NEW,)
    
    # auto generated fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # form auto saves current logged in user
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name="task_creator")


def task_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'task_{0}/{1}'.format(instance.task.id, filename)


class Update(models.Model):
    """
    A generic model that is attached to every task.

    It can be 
    * a file upload
    * a comment
    * TODO: mention (soon)
    * TODO: task change
    * TODO: multiple files
    """

    comment = models.TextField(_("Comment"),
    blank=True,
    null=True,
    help_text=_("Add a comment"))
    file = models.FileField(_("Supporting file"), upload_to=task_directory_path, null=True, blank=True)

    # auto gen field
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE)
    task = models.ForeignKey('tasks.Task', on_delete=models.CASCADE)

    def clean(self):
        """
        Ensure that one of the fields are filled
        """
        print("file is ", self.file)
        if not self.comment and not self.file:
            raise ValidationError(_("You must fill at least one."), code='invalid')
