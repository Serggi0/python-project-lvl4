from django_tables2.utils import A
import django_tables2 as tables
from tasks.models import Task
from django.utils.translation import ugettext as _

class TasksTable(tables.Table):
    TEMPLATE = '''
    <a href="{% url 'tasks:update_task' record.pk %}" class="tbl_icon edit">Edit</a>
    <br>
    <a href="{% url 'tasks:delete_task' record.pk %}" class="tbl_icon delete">Delete</a>
'''
    links = tables.TemplateColumn(TEMPLATE, empty_values=(), verbose_name='')

    class Meta:
        model = Task
        template_name = "django_tables2/bootstrap4.html"
        fields = ('id', 'name', 'description', 'author', 'executor', 'status', 'label', 'create_date', 'links')
        attrs = {
            'class': 'table table-striped'
        }
