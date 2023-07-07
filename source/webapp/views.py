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
                                       )

            return redirect("task_view", pk=task.pk)
        else:
            print(form.errors)
            return render(request, "create_task.html", {"form": form})


def task_update_view(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == "GET":
        form = TaskForm(initial={"title": task.title,
                                 "status": task.status,
                                 "description": task.description,
                                 "detailed_description": task.detailed_description,
                                 })
        return render(request, "update_task.html", {"form": form})
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.status = request.POST.get("status")
            task.title = request.POST.get("title")
            task.description = request.POST.get("description")
            task.detailed_description = request.POST.get("detailed_description")
            task.save()
            return redirect("task_view", pk=task.pk)
        else:
            return render(request, "update_task.html", {"form": form})


class TaskDetailView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = get_object_or_404(Task, id=kwargs['pk'])
        return context

    def get_template_names(self):
        return "task.html"


def task_delete_view(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == "GET":
        return render(request, "delete_task.html", {"task": task})
    else:
        task.delete()
        return redirect("index")
