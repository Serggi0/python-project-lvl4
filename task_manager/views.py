from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.urls.base import reverse_lazy
from django.utils.translation import gettext as _
from django.contrib import messages


def index(request):

    return render(request, 'home.html', context={
        'title': 'Task manager',
    })

# def login(request):
#     return HttpResponse('Авторизация')

class LoginUser(LoginView):
    form_class = AuthenticationForm  # стандартная форма авторизации
    template_name = 'users/login.html'
    extra_context = {'title': 'Entrance'}
    error_messages = {
        'invalid_login': _(
            'The error came out'
        ),
        'inactive': _("This account is inactive."),
    }

    def get_success_url(self):
        messages.info(self.request, 'Hello') # todo text & translate
        return reverse_lazy('home')



def logout_user(request):
    # разлогинивание
    logout(request)
    messages.info(request, 'You are logged out, Good bye') # todo text & translate
    return redirect('home')
