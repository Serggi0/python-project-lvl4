from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView

from django.shortcuts import render

from django.urls.base import reverse_lazy
from django.utils.translation import gettext as _
from django.contrib import messages


def index(request):
    return render(request, 'home.html', context={
        'title': _('Task manager'),
    })


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    extra_context = {'title': _('Entrance')}

    def get_success_url(self):
        messages.success(self.request, _('You are logged in'))
        return reverse_lazy('home')


class LogoutUser(LogoutView):
    def get_next_page(self):
        messages.info(self.request, _('You are logged out, Good bye'))
        return reverse_lazy('home')
