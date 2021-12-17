import django_tables2 as tables
from django.utils.translation import gettext as _
from statuses.models import Status


class StatusesTable(tables.Table):
    TEMPLATE = '''
    <a href="{% url 'statuses:update_status' record.pk %}" class="tbl_icon edit">{{ edit }}</a>
    <br>
    <a href="{% url 'statuses:delete_status' record.pk %}" class="tbl_icon delete">{{ delete }}</a>
'''
    links = tables.TemplateColumn(
        TEMPLATE,
        empty_values=(),
        verbose_name='',
        extra_context={'edit': _('Edit'), 'delete': _('Delete')}
    )

    class Meta:
        model = Status
        template_name = "django_tables2/bootstrap4.html"
        fields = ('id', 'name', 'create_date', 'links')
        attrs = {
            'button_name': _('Create'),
            'class': 'table table-striped'
        }
