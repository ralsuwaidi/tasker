from django.urls import path


from tasker.tasks.views import (
    task_list_view,
    task_detail_view
)

app_name = "tasks"

urlpatterns = [
    path("", view=task_list_view, name="list"),
    path("<int:id>/", view=task_detail_view, name="detail"),
]