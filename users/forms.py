from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')

class UpdateUserForm(UserChangeForm):
    password1 = forms.CharField( label=_("Password"),
        help_text=_('Your password must contain at least 3 characters.'),
        widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    password2 = forms.CharField( label=_("Password confirmation"),
        help_text=_('To confirm, please enter the password again.'),
        widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')


class CreateStatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ('name',)
        labels = {'name': _('Name'),}
        help_texts = {
            'name': _('Some useful help text.'),
        }
        error_messages = {
            'name': {
                'max_length': _("This name is too long."),
            },
        }

class UpdateStatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ('name',)

class DeleteStatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ('name',)


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'author', 'status', 'executor', 'label')
        # labels = {'name': _('Name'),}
        # help_texts = {
        #     'name': _('Some useful help text.'),
        # }
        # error_messages = {
        #     'name': {
        #         'max_length': _("This name is too long."),
        #     },
        # }

class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'author', 'status', 'executor', 'label')

class DeleteTaskForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ('name',)


class CreateLabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ('name',)


class UpdateLabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ('name',)

class DeleteLabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ('name',)