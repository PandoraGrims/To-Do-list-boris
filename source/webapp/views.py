from django.shortcuts import render, redirect, get_object_or_404

from webapp.form import TaskForm
from webapp.models import Task

from django.views import View
from django.views.generic import TemplateView


class TaskListView(View):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.order_by("-status")
        context = {"tasks": tasks}
        return render(request, "index.html", context)


class TaskCreateView(View):
    def get(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        print(form)
        return render(request, "create_task.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(title=form.cleaned_data.get("title"),
                                       detailed_description=form.cleaned_data.get("detailed_description"),
                                       status=form.cleaned_data.get("status"),
                                       type=form.cleaned_data.get("type"),
                                       created_at=form.cleaned_data.get("created_at"),
                                       updated_at=form.cleaned_data.get("updated_at")
                                       )

            return redirect("task_view", pk=task.pk)
        else:
            print(form.errors)
            return render(request, "create_task.html", {"form": form})


class TaskDetailView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = get_object_or_404(Task, id=kwargs['pk'])
        return context

    def get_template_names(self):
        return "task.html"


def task_update_view(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == "GET":
        form = TaskForm(initial={"title": task.title,
                                 "status": task.status,
                                 "type": task.type,
                                 "detailed_description": task.detailed_description,
                                 })
        return render(request, "update_task.html", {"form": form})
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():

            task.title = form.cleaned_data.get("title")
            task.content = form.cleaned_data.get("detailed_description")
            task.author = form.cleaned_data.get("author")
            task.type = form.cleaned_data.get("type")
            task.status = form.cleaned_data.get("status")
            task.save()
            return redirect("task_view", pk=task.pk)
        else:
            return render(request, "update_task.html", {"form": form})


def task_delete_view(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == "GET":
        return render(request, "delete_task.html", {"task": task})
    else:
        task.delete()
        return redirect("index")
