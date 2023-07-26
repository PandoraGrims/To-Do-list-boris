from django.urls import path

from webapp.views.tasks_view import TaskUpdateView, TaskCreateView, TaskDetailView, TaskDeleteView, \
    ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView, AddUserToProjectView

app_name = "webapp"

urlpatterns = [
    path('', ProjectListView.as_view(), name="index"),
    path('projects/<int:pk>', ProjectDetailView.as_view(), name="project_detail_view"),
    path('project/add/', ProjectCreateView.as_view(), name="project_add"),
    path('project/<int:pk>/update', ProjectUpdateView.as_view(), name="project_update_view"),
    path('project/<int:pk>/delete', ProjectDeleteView.as_view(), name="project_delete_view"),
    path('project/<int:pk>/tasks/add/', TaskCreateView.as_view(), name="task_add"),
    path('tasks/<int:pk>', TaskDetailView.as_view(), name="task_view"),
    path('tasks/<int:pk>/update', TaskUpdateView.as_view(), name="task_update_view"),
    path('tasks/<int:pk>/delete', TaskDeleteView.as_view(), name="task_delete_view"),
    path('project/<int:pk>/add_user/', AddUserToProjectView.as_view(), name='add_user_to_project'),
    # path('project/<int:pk>/remove_user/<int:user_pk>/', views.RemoveUserFromProjectView.as_view(),
    #      name='remove_user_from_project'),
]
