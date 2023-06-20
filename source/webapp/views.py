from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from webapp.models import Task


def task_list_view(request):
    tasks = Task.objects.order_by("-updated_at")
    context = {"tasks": tasks}
    return render(request, "index.html", context)


def task_create_view(request):
    if request.method == "GET":
        return render(request, "create_task.html")
    else:
        Task.objects.create(
            title=request.POST.get("title"),
            description=request.POST.get("description"),
            author=request.POST.get("author")
        )
        return HttpResponseRedirect("/")


def task_view(request):
    task_id = request.GET.get("id")
    task = Task.objects.get(id=task_id)
    return render(request, "task.html", {"task": task})


def delete_task(request):
    task_id = request.GET.get("id")
    task = Task.objects.get(Task, id=task_id)
    task.delete()
    return redirect('task_list')
