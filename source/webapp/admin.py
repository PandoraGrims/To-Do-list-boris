from django.contrib import admin

from webapp.models import Task, Type, Status

admin.site.register(Type)

admin.site.register(Status)


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'detailed_description']
    fields = ['title', 'detailed_description', 'status', 'type']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Task, TaskAdmin)
