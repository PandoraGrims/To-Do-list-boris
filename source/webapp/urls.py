from django.urls import path


from webapp.views.tasks_view import TaskListView, task_update_view, TaskCreateView, TaskDetailView, task_delete_view

urlpatterns = [
    path('', TaskListView.as_view(), name="index"),
    path('task/add/', TaskCreateView.as_view(), name="task_add"),
    path('task/<int:pk>', TaskDetailView.as_view(), name="task_view"),
    path('task/<int:pk>/update', task_update_view, name="task_update_view"),
    path('task/<int:pk>/delete', task_delete_view, name="task_delete_view"),
]
