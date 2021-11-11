from django import forms
from django.utils.translation import gettext as _

from tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'status', 'executor', 'label')


class DeleteTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name',)
