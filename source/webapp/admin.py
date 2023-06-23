from django.contrib import admin

from webapp.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'data_field', 'status']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'description', 'detailed_description']
    fields = ['title', 'description', 'detailed_description', 'data_field', 'status']
    readonly_fields = ['data_field']


admin.site.register(Task, TaskAdmin)
