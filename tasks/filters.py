import django_filters as filters
from tasks.models import Task
from django.utils.translation import gettext as _


class TaskFilter(filters.FilterSet):
    '''
    Объявление фильтруемыми поля fields. См. class TasksView
    '''
    class Meta:
        model = Task
        fields = ['status', 'label', 'executor']
