from django import forms
from django.utils.translation import gettext as _

from tasks.models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('name', 'description', 'status', 'executor', 'label')
        labels = {'label': _('Labels')}

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['executor'].empty_label = ''
