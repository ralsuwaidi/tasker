from django.contrib import admin

from .models import Task, Update

admin.site.register(Task)
admin.site.register(Update)
