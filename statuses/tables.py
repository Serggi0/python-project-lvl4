from django_tables2.utils import A
import django_tables2 as tables
from statuses.models import Status
from django.utils.translation import ugettext as _



class StatusesTable(tables.Table):
    TEMPLATE = '''
    <a href="{% url 'statuses:update_status' record.pk %}" class="tbl_icon edit">Edit</a>
    <br>
    <a href="{% url 'statuses:delete_status' record.pk %}" class="tbl_icon delete">Delete</a>
'''
    links = tables.TemplateColumn(TEMPLATE, empty_values=(), verbose_name='')

    class Meta:
        model = Status
        template_name = "django_tables2/bootstrap4.html"
        fields = ('id', 'name', 'create_date', 'links')
        attrs = {
            'button_name': 'Create',
            'class': 'table table-striped'
        }
