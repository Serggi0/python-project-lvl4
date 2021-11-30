import django_filters as filters
from django.forms.widgets import CheckboxInput
from django.utils.translation import gettext as _

from tasks.models import Task
from labels.models import Label


class TaskFilter(filters.FilterSet):
    '''
    Объявление фильтруемыми поля fields. См. class TasksView
    '''
    own_tasks = filters.BooleanFilter(
        label=_('Only your own tasks'),
        method='filter_own_tasks',
        widget=CheckboxInput
    )

    def filter_own_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user.pk)
        return queryset

    label = filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label=_('Label')
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'label', 'own_tasks']
