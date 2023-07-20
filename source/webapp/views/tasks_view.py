from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils.html import urlencode
from webapp.form import TaskForm, SearchForm, ProjectForm
from webapp.models import Task, Project

from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView


class ProjectListView(ListView):
    model = Project
    template_name = 'project/project_list_view.html'
    context_object_name = 'projects'
    ordering = ("-start_date",)
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        search_value = self.request.GET.get('search')
        if search_value:
            queryset = queryset.filter(Q(name__icontains=search_value) | Q(description__icontains=search_value))
        return queryset


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project/project_detail_view.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.get_object()
        tasks = project.tasks.all()
        context['tasks'] = tasks
        return context


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "project/project_create_view.html"

    def get_success_url(self):
        return reverse("project_detail_view", kwargs={"pk": self.object.pk})


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = "project/project_update_view.html"

    def get_success_url(self):
        return reverse("project_detail_view", kwargs={"pk": self.object.pk})


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = "project/project_delete_view.html"
    success_url = reverse_lazy("index")


class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task.html'
    context_object_name = 'task'


class TaskCreateView(CreateView):
    form_class = TaskForm
    template_name = "tasks/create_task.html"
    success_url = reverse_lazy("task_view")

    def get_success_url(self):
        return reverse("task_view", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get("pk"))
        task = form.save(commit=False)
        task.project = project
        task.save()
        return redirect("project_detail_view", pk=project.pk)


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/update_task.html"
    success_url = reverse_lazy("task_view")

    def get_success_url(self):
        return reverse("task_view", kwargs={"pk": self.object.pk})


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tasks/delete_task.html"
    success_url = reverse_lazy("index")
