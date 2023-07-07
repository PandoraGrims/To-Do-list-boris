from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect

from webapp.form import TaskForm
from webapp.models import Task, status_choices

from django.views import View
from django.views.generic import TemplateView


class TaskListView(View):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.order_by("data_field")
        context = {"tasks": tasks}
        return render(request, "index.html", context)


def task_list_view(request):
    tasks = Task.objects.order_by("-data_field")
    context = {"tasks": tasks}
    return render(request, "index.html", context)


class ArticleCreateView(View):
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        print(form)
        return render(request, "create_task.html", {"status_choices": status_choices, "form": form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            tags = form.cleaned_data.pop("tags")
            task = Task.objects.create(title=form.cleaned_data.get("title"),
                                          description=form.cleaned_data.get("description"),
                                          detailed_description=form.cleaned_data.get("detailed_description"),
                                          status=form.cleaned_data.get("status"),
                                          data_field=form.cleaned_data.get("data_field")
                                          )
            task.tags.set(tags)
            return redirect("task_view", pk=task.pk)
        else:
            print(form.errors)
            return render(request, "create_article.html", {"form": form})


def task_create_view(request):
    if request.method == "GET":
        form = TaskForm()
        return render(request, "create_task.html", {"status_choices": status_choices, "form": form})
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(title=form.cleaned_data.get("title"),
                                       description=form.cleaned_data.get("description"),
                                       detailed_description=form.cleaned_data.get("detailed_description"),
                                       status=form.cleaned_data.get("status"),
                                       data_field=form.cleaned_data.get("data_field"))
            return redirect("task_view", pk=task.pk)
        else:
            return render(request, "create_task.html", {"status_choices": status_choices, "form": form})


def task_update_view(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == "GET":
        form = TaskForm(initial={"title": task.title,
                                 "status": task.status,
                                 "description": task.description,
                                 "detailed_description": task.detailed_description,
                                 "data_field": task.data_field
                                 })
        return render(request, "update_task.html", {"status_choices": status_choices, "form": form})
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.status = request.POST.get("status")
            task.title = request.POST.get("title")
            task.description = request.POST.get("description")
            task.detailed_description = request.POST.get("detailed_description")
            task.data_field = request.POST.get("data_field")
            task.save()
            return redirect("task_view", pk=task.pk)
        else:
            return render(request, "update_task.html", {"form": form})


def task_view(request, *args, pk, **kwargs):
    task = Task.objects.get(id=pk)
    return render(request, "task.html", {"task": task})


def task_delete_view(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == "GET":
        return render(request, "delete_task.html", {"task": task})
    else:
        task.delete()
        return redirect("index")
