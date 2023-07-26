from django.contrib import admin

from webapp.models import Task, Type, Status, Project, User


admin.site.register(Type)

admin.site.register(Status)

admin.site.register(Task)

admin.site.register(Project)

