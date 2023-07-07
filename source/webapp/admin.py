from django.contrib import admin

from webapp.models import Task, Type, Status

admin.site.register(Type)

admin.site.register(Status)


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'data_field', 'status', 'type']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'detailed_description']
    fields = ['title', 'detailed_description', 'data_field', 'status']
    readonly_fields = ['data_field']


admin.site.register(Task, TaskAdmin)
