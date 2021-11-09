from django import forms
from django.utils.translation import gettext as _

from .models import Status


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ('name',)
        # labels = {'name': _('Name'),}
        # help_texts = {
        #     'name': _('Some useful help text.'),
        # }
        # error_messages = {
        #     'name': {
        #         'max_length': _("This name is too long."),
        #     },
        # }


# class UpdateStatusForm(forms.ModelForm):
#     class Meta:
#         model = Status
#         fields = ('name',)


# class DeleteStatusForm(forms.ModelForm):
#     class Meta:
#         model = Status
#         fields = ('name',)


