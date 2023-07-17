from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.utils.html import urlencode
from webapp.form import TaskForm, SearchForm
from webapp.models import Task, Project

from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

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


class TaskCreateView(View):
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, "tasks/create_task.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():

            types = form.cleaned_data.pop("type")

            task = Task.objects.create(title=form.cleaned_data.get("title"),
                                       detailed_description=form.cleaned_data.get("detailed_description"),
                                       status=form.cleaned_data.get("status"),
                                       created_at=form.cleaned_data.get("created_at"),
                                       updated_at=form.cleaned_data.get("updated_at")
                                       )
            task.type.set(types)
            return redirect("task_view", pk=task.pk)
        else:
            return render(request, "tasks/create_task.html", {"form": form})


class TaskDetailView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = get_object_or_404(Task, id=kwargs['pk'])
        return context

    def get_template_names(self):
        return "tasks/tasks.html"


def task_update_view(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == "GET":
        form = TaskForm(initial={"title": task.title,
                                 "status": task.status,
                                 "types": task.type.all(),
                                 "detailed_description": task.detailed_description,
                                 })
        return render(request, "tasks/update_task.html", {"form": form})
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            types = form.cleaned_data.pop("type")
            task.title = form.cleaned_data.get("title")
            task.content = form.cleaned_data.get("detailed_description")
            task.author = form.cleaned_data.get("author")
            task.status = form.cleaned_data.get("status")
            task.save()
            task.type.set(types)
            return redirect("task_view", pk=task.pk)
        else:
            return render(request, "tasks/update_task.html", {"form": form})


def task_delete_view(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == "GET":
        return render(request, "tasks/delete_task.html", {"tasks": task})
    else:
        task.delete()
        return redirect("index")
