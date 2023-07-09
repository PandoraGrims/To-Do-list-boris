from django import forms

from webapp.models import Type, Status


class TypeForm(forms.Form):
    type_name = forms.CharField(max_length=50, required=True, label="Тип")


class StatusForm(forms.Form):
    status_name = forms.CharField(max_length=50, required=True, label="Тип")


class TaskForm(forms.Form):
    status = forms.ModelChoiceField(queryset=Status.objects.all(), label="Статус")
    type = forms.ModelChoiceField(queryset=Type.objects.all(), label="Тип")
    title = forms.CharField(max_length=50, required=True, label="Название")
    detailed_description = forms.CharField(max_length=50, required=True, label="Подробное описание")
