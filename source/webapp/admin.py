from django.contrib import admin

from webapp.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'created_at']
    list_display_links = ['id', 'title']
    list_filter = ['author']
    search_fields = ['title', 'description']
    fields = ['title', 'author', 'description', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Task, TaskAdmin)
