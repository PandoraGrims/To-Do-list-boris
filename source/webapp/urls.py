from django.urls import path

from webapp.views import task_list_view, task_create_view, task_view, delete_task

urlpatterns = [
    path('', task_list_view),
    path('task/add/', task_create_view),
    path('task/', task_view),
    path('delete/<int:task_id>/', delete_task),
]
