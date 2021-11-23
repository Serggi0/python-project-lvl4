from django.contrib.auth.forms import UserCreationForm

from users.models import User


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2'
        )

# class UpdateUserForm(UserChangeForm):
    # password1 = forms.CharField(
    #     label=_("Password"),
    #     help_text=_('Your password must contain at least 3 characters.'),
    #     widget=forms.PasswordInput(attrs={'class': 'form-input'})
    # )

    # password2 = forms.CharField(
    #     label=_("Password confirmation"),
    #     help_text=_('To confirm, please enter the password again.'),
    #     widget=forms.PasswordInput(attrs={'class': 'form-input'})
    # )

    # class Meta:
    #     model = User
    #     fields = (
    #         'first_name',
    #         'last_name',
    #         'username',
    #         'password1',
    #         'password2'
    #     )
