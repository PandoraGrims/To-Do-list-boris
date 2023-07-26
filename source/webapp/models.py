from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Название')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    start_date = models.DateField(null=False, blank=False, verbose_name='Дата начала')
    end_date = models.DateField(null=True, blank=True, verbose_name='Дата окончания')
    user = models.ManyToManyField(User, related_name='projects', verbose_name='Юзер', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'projects'
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Type(models.Model):
    type_name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Тип')

    def __str__(self):
        return self.type_name

    class Meta:
        db_table = "types"
        verbose_name = "Тип"
        verbose_name_plural = "Типы"


class Status(models.Model):
    status_name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Статус')

    def __str__(self):
        return self.status_name

    class Meta:
        db_table = "statuses"
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class Task(models.Model):
    status = models.ForeignKey('webapp.Status', on_delete=models.CASCADE, related_name='statuses', blank=True)
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Название")
    detailed_description = models.TextField(max_length=2000, verbose_name="Подробное описание", null=True, blank=True,
                                            default=None)
    type = models.ManyToManyField('webapp.Type', related_name='tasks', through='webapp.TaskType',
                                  through_fields=('task', 'type'), blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks', verbose_name='Проект')

    def __str__(self):
        return f"{self.pk} {self.title}"

    class Meta:
        db_table = "tasks"
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"


class TaskType(models.Model):
    task = models.ForeignKey('webapp.Task', related_name='task_types', on_delete=models.CASCADE,
                             verbose_name='Задача')
    type = models.ForeignKey('webapp.Type', related_name='type_tasks', on_delete=models.CASCADE, verbose_name='Тип')

    def __str__(self):
        return "{} | {}".format(self.task, self.type)
