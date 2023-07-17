from django.contrib import admin

from webapp.models import Task, Type, Status, Project


admin.site.register(Type)

admin.site.register(Status)

admin.site.register(Task)

admin.site.register(Project)













#
# class TaskAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title']
#     list_display_links = ['id', 'title']
#     search_fields = ['title', 'detailed_description']
#     fields = ['title', 'detailed_description', 'status', 'type']
#     readonly_fields = ['created_at', 'updated_at']
#
