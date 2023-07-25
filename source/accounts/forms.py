from django.contrib.auth.forms import UserCreationForm
from django.forms import forms

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MyUserCreationForm(UserCreationForm):
    # first_name = forms.CharField(max_length=30, required=False, label='Имя')
    # last_name = forms.CharField(max_length=30, required=False, label='Фамилия')
    password = forms.CharField(label="Пароль", strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Подтвердите пароль", required=True, widget=forms.PasswordInput,
                                       strip=False)
    email = forms.EmailField(required=True, label='Email')

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают!')

        if not first_name and not last_name:
            raise forms.ValidationError('Введите хотя бы одно из полей "Имя" или "Фамилия".')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password', 'password_confirm', 'first_name', 'last_name', 'email']
