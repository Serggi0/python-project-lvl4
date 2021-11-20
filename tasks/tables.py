import django_tables2 as tables

from tasks.models import Task


class TasksTable(tables.Table):
    TEMPLATE = '''
    <a href="{% url 'tasks:update_task' record.pk %}" class="tbl_icon edit">Edit</a>
    <br>
    <a href="{% url 'tasks:delete_task' record.pk %}" class="tbl_icon delete">Delete</a>
'''
    links = tables.TemplateColumn(TEMPLATE, empty_values=(), verbose_name='')
    name = tables.TemplateColumn('<a href="{% url \'tasks:view_task\' record.pk %}">{{ record.name }}</a>')

    class Meta:
        model = Task
        template_name = "django_tables2/bootstrap4.html"
        fields = ('id', 'name', 'status', 'author', 'executor', 'create_date', 'links')
        attrs = {
            'class': 'table table-striped'
        }
