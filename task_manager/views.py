from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView

from django.shortcuts import render

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
    error_message = '!!!'
    # _("Please enter a correct %(username)s and password. Note that both ")

    # def get_invalid_login_error(self):
    #     # messages.add_message(
    #     #     self.request,
    #     #     messages.error,
    #     #     '!!!!')
    #     return redirect(self.login_url)

    def get_success_url(self):
        messages.success(self.request, _('You are logged in'))
        return reverse_lazy('home')


class LogoutUser(LogoutView):

    def get_next_page(self):
        # messages.add_message(
        #     self.request, messages.SUCCESS,
        #     _('You are logged out, Good bye')
        # )
        messages.info(self.request, _('You are logged out, Good bye'))
        return reverse_lazy('home')

# def logout_user(request):
#     # разлогинивание
#     logout(request)
#     messages.info(request, 'You are logged out, Good bye')
#     return redirect('home')
