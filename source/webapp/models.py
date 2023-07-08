from django.db import models


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
    type = models.ForeignKey('webapp.Type', on_delete=models.CASCADE, related_name='types', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    def __str__(self):
        return f"{self.pk} {self.title}"

    class Meta:
        db_table = "tasks"
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
