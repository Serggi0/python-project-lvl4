import django_filters as filters
from .models import Task
from django.utils.translation import gettext as _


class TaskFilter(filters.FilterSet):

    class Meta:
        model = Task
        fields = ['status', 'label', 'executor']
