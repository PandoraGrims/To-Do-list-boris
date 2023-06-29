from django.urls import path

from webapp.views import task_list_view, task_update_view, task_create_view, task_view

urlpatterns = [
    path('', task_list_view, name="index"),
    path('task/add/', task_create_view, name="task_add"),
    path('task/<int:pk>', task_view, name="task_view"),
    path('task/<int:pk>/update', task_update_view, name="task_update_view"),
]
