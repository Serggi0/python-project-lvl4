from django.urls.base import reverse_lazy
from django.views import generic
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django_tables2 import SingleTableView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import ugettext as _

from task_manager import user_messages
from users.forms import UserForm
from users.tables import UsersTable
from users.models import User
from tasks.models import Task


class UsersView(SingleTableView):
    model = User
    # users = Users.objects.all()
    table_class = UsersTable
    template_name = 'users/users.html'
    # замена имени шаблона вместо дефолтного 'users_list'
    # context_object_name = 'all_users_list'
    # замена названия коллекции для html-файла вместо дефолтного object_list
    extra_context = {'title': _('Users')}
    # добавление заголовка страницы через атрибут extra_context

    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #     return super().get_context_data(**kwargs)


class CreateUser(SuccessMessageMixin, generic.CreateView):
    form_class = UserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')
    # https://youtu.be/QK4qbVyY7oU?list=PLA0M1Bcd0w8xO_39zZll2u1lz_Q-Mwn1F
    success_message = user_messages.SUCCES_MESSAGE_CREATE_USER
    # ! https://djangodoc.ru/3.1/ref/contrib/messages/
    extra_context = {
        'title': 'Registration',
        'button_name': _('Register')
    }

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     c_def = self.get_user_context(title="Registration")
    #     return dict(list(context.items()) + list(c_def.items()))


class UpdateUser(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView
):
    login_url = 'login'
    model = User
    form_class = UserForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users:users')
    extra_context = {'title': _('Update user')}
    success_message = user_messages.SUCCES_MESSAGE_UPDATE_USER
    error_message = user_messages.ERROR_MESSAGE_NOT_LOGGED

    def handle_no_permission(self):
        messages.error(
            self.request,
            self.error_message
        )
        return redirect(self.login_url)

    def test_func(self):
        obj = self.get_object()
        if (self.request.user.is_authenticated
            and obj.pk != self.request.user.pk):
            self.error_message = user_messages.ERROR_MESSAGE_NOT_RIGHTS
            self.login_url = reverse_lazy('users:users')
            return False
        return True

# def create(request):
#     return HttpResponse('Регистрация пользователя')

# def update_user(request, user_id):
#     return HttpResponse(f'Редактирование пользователя {user_id}')

# def delete_user(request, user_id):
#     u = Users.objects.get(pk=user_id)
#     u.delete()
#     return HttpResponse(f'Удаление пользователя {user_id}')


class DeleteUser(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView
):
    login_url = 'login'
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users:users')
    extra_context = {'title': _('Delete user')}
    success_message = user_messages.SUCCES_MESSAGE_DELETE_USER
    error_message = user_messages.ERROR_MESSAGE_NOT_LOGGED

    def handle_no_permission(self):
        messages.error(
            self.request,
            self.error_message
        )
        return redirect(self.login_url)

    def delete(self, request, *args, **kwargs):
        '''
        class DeletionMixin. Вызывается метод delete()
        и перенаправляется на URL после успешного удаления объекта
        '''
        if Task.objects.filter(
            author=self.request.user.pk
        ) or Task.objects.filter(
            executor=self.request.user.pk
        ):
            messages.error(
                self.request,
                user_messages.ERROR_MESSAGE_NOT_POSSIBLE_DELETE_USER
            )
            return redirect(reverse_lazy('users:users'))
        messages.success(
            self.request,
            self.success_message
        )
        return super().delete(request, *args, **kwargs)

    def test_func(self):
        self.object = self.get_object()
        if self.object.pk == self.request.user.pk:
            return True
        else:
            self.error_message = user_messages.ERROR_MESSAGE_NOT_RIGHTS
            self.login_url = reverse_lazy('users:users')
            return False
