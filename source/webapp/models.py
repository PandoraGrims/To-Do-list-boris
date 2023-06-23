from django.db import models

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class Task(models.Model):
    status = models.CharField(max_length=50, null=False, blank=False, verbose_name="Статус", choices=status_choices,
                              default=status_choices[0][0])
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Название")
    description = models.TextField(max_length=1000, verbose_name="Описание")
    detailed_description = models.TextField(max_length=2000, verbose_name="Подробное описание", null=True, blank=True,
                                            default=None)
    data_field = models.DateField(verbose_name="Дата создания", null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.pk} {self.title}"

    class Meta:
        db_table = "tasks"
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
