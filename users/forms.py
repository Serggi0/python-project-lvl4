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


class CreateStatusForm():
    class Meta:
        model = Statuses
        fields = ('name',)

class UpdateStatusForm():
    class Meta:
        model = Statuses
        fields = ('name',)
