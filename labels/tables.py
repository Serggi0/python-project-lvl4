import django_tables2 as tables
from django.utils.translation import ugettext as _
from labels.models import Label


class LabelsTable(tables.Table):
    TEMPLATE = '''
    <a href="{% url 'labels:update_label' record.pk %}" class="tbl_icon edit">{{ edit }}</a>
    <br>
    <a href="{% url 'labels:delete_label' record.pk %}" class="tbl_icon delete">{{ delete }}</a>
'''
    links = tables.TemplateColumn(
        TEMPLATE,
        empty_values=(),
        verbose_name='',
        extra_context={'edit': _('Edit'), 'delete': _('Delete')}
    )

    class Meta:
        model = Label
        template_name = "django_tables2/bootstrap4.html"
        fields = ('id', 'name', 'create_date', 'links')
        attrs = {
            'class': 'table table-striped'
        }
