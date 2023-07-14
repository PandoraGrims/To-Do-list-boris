from django.shortcuts import render, redirect, get_object_or_404

from webapp.form import TaskForm
from webapp.models import Task

from django.views import View
from django.views.generic import TemplateView, ListView


class TaskListView(ListView):
    model = Task
    template_name = "tasks/index.html"
    context_object_name = "tasks"
    ordering = ("-updated_at", )

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(title__contains="Задач")

    # def get(self, request, *args, **kwargs):
    #     tasks = Task.objects.order_by("-updated_at")
    #     context = {"tasks": tasks}
    #     return render(request, "tasks/index.html", context)
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        return context

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
