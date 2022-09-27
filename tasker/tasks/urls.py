from django.urls import path


from tasker.tasks.views import (
    task_list_view,
    task_detail_view,
    task_create_view,
    task_update_view,
    task_delete_view,
    update_create_view
)

app_name = "tasks"

urlpatterns = [
    path("", view=task_list_view, name="list"),
    path("<int:id>/", view=task_detail_view, name="detail"),
    path("~create/", view=task_create_view, name="create"),
    path("<int:id>/~update/", view=task_update_view, name="update"),
    path("<int:id>/~delete/", view=task_delete_view, name="delete"),
]

# update per task
urlpatterns += [
    path("<int:task_id>/update/create", view=update_create_view, name="update_create"),
]