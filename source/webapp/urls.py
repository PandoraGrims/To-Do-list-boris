from django.urls import path

from webapp.views.tasks_view import TaskListView, task_update_view, TaskCreateView, TaskDetailView, task_delete_view, \
    ProjectListView, ProjectDetailView, ProjectCreateView

urlpatterns = [
    path('', ProjectListView.as_view(), name="index"),
    path('projects/<int:pk>', ProjectDetailView.as_view(), name="project_detail_view"),
    path('project/add/', ProjectCreateView.as_view(), name="project_add"),
    path('tasks_list/', TaskListView.as_view(), name="tasks_list"),
    path('tasks/add/', TaskCreateView.as_view(), name="task_add"),
    path('tasks/<int:pk>', TaskDetailView.as_view(), name="task_view"),
    path('tasks/<int:pk>/update', task_update_view, name="task_update_view"),
    path('tasks/<int:pk>/delete', task_delete_view, name="task_delete_view"),
]



