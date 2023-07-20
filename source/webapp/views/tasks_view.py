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


class TaskListView(ListView):
    model = Task
    template_name = "tasks/index.html"
    context_object_name = "tasks"
    ordering = ("-updated_at",)
    paginate_by = 3

    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context["form"] = self.form
        if self.search_value:
            context["query"] = urlencode({'search': self.search_value})
            context["search_value"] = self.search_value
        return context

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

    def get_queryset(self):
        queryset = super().get_queryset()
        print(self.search_value)
        if self.search_value:
            queryset = queryset.filter(Q(title__icontains=self.search_value) |
                                       Q(detailed_description__icontains=self.search_value))

            return queryset
        else:
            return queryset


class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task.html'
    context_object_name = 'task'



class TaskCreateView(CreateView):
    form_class = TaskForm
    template_name = "tasks/create_task.html"
    success_url = reverse_lazy("task_view")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/update_task.html"
    success_url = reverse_lazy("task_view")

    def get_success_url(self):
        return reverse("task_view", kwargs={"pk": self.object.pk})


class ArticleDeleteView(DeleteView):
    model = Task
    template_name = "tasks/delete_task.html"
    success_url = reverse_lazy("index")
