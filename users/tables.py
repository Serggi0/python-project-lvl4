import django_tables2 as tables
from users.models import User
from django.utils.translation import ugettext as _


# https://overcoder.net/q/262100/django-tables2-linkcolumn-%D0%BD%D0%B5%D1%81%D0%BA%D0%BE%D0%BB%D1%8C%D0%BA%D0%BE-%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D0%BE%D0%B2-%D0%B2-%D0%BE%D0%B4%D0%BD%D0%BE%D0%B9-%D1%8F%D1%87%D0%B5%D0%B9%D0%BA%D0%B5


class UsersTable(tables.Table):
    TEMPLATE = '''
    <a href="{% url 'users:update_user' record.pk %}" class="tbl_icon edit">Edit</a>
    <br>
    <a href="{% url 'users:delete_user' record.pk %}" class="tbl_icon delete">Delete</a>
'''
    # ! https://coderedirect.com/questions/365855/django-tables2-create-extra-column-with-links

    links = tables.TemplateColumn(TEMPLATE, empty_values=(), verbose_name='')

    class Meta:
        model = User
        template_name = "django_tables2/bootstrap4.html"
        fields = ('id', 'username', 'full_name', 'date_joined', 'links')
        attrs = {
            'class': 'table table-striped'
        }

