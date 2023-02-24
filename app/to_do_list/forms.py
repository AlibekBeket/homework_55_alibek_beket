from datetime import time, datetime

from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from to_do_list.models import ToDo


class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ('title', 'description', 'status', 'date')
        labels = {
            'title': 'Заголовок',
            'description': 'Описание',
            'status': 'Статус',
            'date': 'Дата'
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 3 or title[0] == " ":
            raise ValidationError('Заголовок должен быть больше 2 символов и не должен начинаться на пробел')
        return title
