from django import forms

from webapp.models import Type, Status


class TaskForm(forms.Form):
    status = forms.ModelMultipleChoiceField(queryset=Status.objects.all(), label="Статус")
    type = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), label="Тип")
    title = forms.CharField(max_length=50, required=True, label="Название")
    detailed_description = forms.CharField(max_length=50, required=True, label="Подробное описание")