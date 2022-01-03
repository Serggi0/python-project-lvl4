import django_tables2 as tables
from django.utils.translation import gettext as _
from users.models import User


class UsersTable(tables.Table):
    TEMPLATE = '''
    <a href="{% url 'users:update_user' record.pk %}" class="tbl_icon edit">{{ edit }}</a>
    <br>
    <a href="{% url 'users:delete_user' record.pk %}" class="tbl_icon delete">{{ delete }}</a>
'''

    links = tables.TemplateColumn(
        TEMPLATE,
        empty_values=(),
        verbose_name='',
        extra_context={'edit': _('Edit'), 'delete': _('Delete')}
    )

    full_name = tables.Column(
        accessor='full_name',
        verbose_name=_('Full name'),
    )

    create_date = tables.DateTimeColumn(
        accessor='date_joined',
        verbose_name=_('Create date')
    )

    class Meta:
        model = User
        template_name = "django_tables2/bootstrap4.html"
        fields = ('id', 'username', 'full_name', 'create_date', 'links')
        attrs = {
            'class': 'table table-striped'
        }
