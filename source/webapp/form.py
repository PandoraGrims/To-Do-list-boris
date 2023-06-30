from django import forms

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class TaskForm(forms.Form):
    status = forms.ChoiceField(required=True, label="Статус", choices=status_choices)
    title = forms.CharField(max_length=50, required=True, label="Название")
    description = forms.CharField(max_length=50, required=True, label="Описание")
    detailed_description = forms.CharField(max_length=50, required=True, label="Подробное описание")
    data_field = forms.DateField(label="Дата создания", required=True)
