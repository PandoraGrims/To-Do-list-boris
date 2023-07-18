from django.urls import path

from webapp.views.tasks_view import TaskListView, TaskUpdateView, TaskCreateView, TaskDetailView, ArticleDeleteView, \
    ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView

urlpatterns = [
    path('', ProjectListView.as_view(), name="index"),
    path('projects/<int:pk>', ProjectDetailView.as_view(), name="project_detail_view"),
    path('project/add/', ProjectCreateView.as_view(), name="project_add"),
    path('project/<int:pk>/update', ProjectUpdateView.as_view(), name="project_update_view"),
    path('project/<int:pk>/delete', ProjectDeleteView.as_view(), name="project_delete_view"),
    path('tasks_list/', TaskListView.as_view(), name="tasks_list"),
    path('tasks/add/', TaskCreateView.as_view(), name="task_add"),
    path('tasks/<int:pk>', TaskDetailView.as_view(), name="task_view"),
    path('tasks/<int:pk>/update', TaskUpdateView.as_view(), name="task_update_view"),
    path('tasks/<int:pk>/delete', ArticleDeleteView.as_view(), name="task_delete_view"),
]



