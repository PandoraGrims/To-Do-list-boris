from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from webapp.models import Type, Status, Task



def validate_title(value):
    if len(value) < 4:
        raise ValidationError('Summary must be greater than four')


def validate_detailed_description(value):
    if 'N-word' in value:
        raise ValidationError('Description contains a bad word')


class TypeForm(forms.Form):
    type_name = forms.CharField(max_length=50, required=True, label="Тип")


class StatusForm(forms.Form):
    status_name = forms.CharField(max_length=50, required=True, label="Тип")


class TaskForm(forms.Form):
    status = forms.ModelChoiceField(queryset=Status.objects.all(), label="Статусы")
    type = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), label="Тип")
    title = forms.CharField(max_length=50, required=True, label="Название")
    detailed_description = forms.CharField(max_length=50, required=True, label="Подробное описание")

    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)

        for v in self.visible_fields():
            if not isinstance(v.field.widget, widgets.CheckboxSelectMultiple):
                v.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Task
        fields = ["title", "detailed_description", "status", "type"]

