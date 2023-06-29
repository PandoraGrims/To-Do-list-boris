from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect

from webapp.models import Task, status_choices


def task_list_view(request):
    tasks = Task.objects.order_by("-data_field")
    context = {"tasks": tasks}
    return render(request, "index.html", context)


def task_create_view(request):
    if request.method == "GET":
        return render(request, "create_task.html", {"status_choices": status_choices})
    else:
        task = Task.objects.create(
            title=request.POST.get("title"),
            description=request.POST.get("description"),
            detailed_description=request.POST.get("detailed_description"),
            status=request.POST.get("status"),
            data_field=request.POST.get("data_field"),
        )

        return redirect("task_view", pk=task.pk)


def task_update_view(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == "GET":
        return render(request, "update_task.html", {"task": task})
    else:

        task.title = request.POST.get("title")
        task.description = request.POST.get("description")
        task.detailed_description = request.POST.get("detailed_description")
        task.status = request.POST.get("status")
        task.data_field = request.POST.get("data_field")
        task.save()
        return redirect("task_view", pk=task.pk)


def task_view(request, *args, pk, **kwargs):
    task = Task.objects.get(id=pk)
    return render(request, "task.html", {"task": task})
