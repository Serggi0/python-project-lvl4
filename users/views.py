from django.urls.base import reverse_lazy
from django.views import generic
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django_tables2 import SingleTableView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _

from task_manager import user_messages
from users.forms import UserForm
from users.tables import UsersTable
from users.models import User
from tasks.models import Task
from task_manager.utils import HandleNoPermissionMixin


class UsersView(SingleTableView):
    model = User
    table_class = UsersTable
    template_name = 'users/users.html'
    extra_context = {'title': _('Users')}


class CreateUser(
    HandleNoPermissionMixin,
    SuccessMessageMixin, generic.CreateView
):
    form_class = UserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')
    success_message = user_messages.SUCCES_MESSAGE_CREATE_USER
    extra_context = {
        'title': 'Registration',
        'button_name': _('Register')
    }
    url_if_user_is_authenticated = 'users:users'
    error_message_user_is_authenticated = (
        user_messages.ERROR_MESSAGE_NOT_RIGHTS
    )
    error_message_not_logged = user_messages.ERROR_MESSAGE_NOT_LOGGED


class UpdateUser(
    HandleNoPermissionMixin,
    LoginRequiredMixin, UserPassesTestMixin,
    SuccessMessageMixin, UpdateView
):
    login_url = 'login'
    model = User
    form_class = UserForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users:users')
    extra_context = {'title': _('Update user')}
    success_message = user_messages.SUCCES_MESSAGE_UPDATE_USER
    url_if_user_is_authenticated = 'users:users'
    error_message_user_is_authenticated = (
        user_messages.ERROR_MESSAGE_NOT_RIGHTS
    )
    error_message_not_logged = user_messages.ERROR_MESSAGE_NOT_LOGGED

    def test_func(self):
        object = self.get_object()
        return object.pk == self.request.user.pk


class DeleteUser(
    HandleNoPermissionMixin,
    LoginRequiredMixin, UserPassesTestMixin,
    SuccessMessageMixin, DeleteView
):
    login_url = 'login'
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users:users')
    extra_context = {'title': _('Delete user')}
    success_message = user_messages.SUCCES_MESSAGE_DELETE_USER
    url_if_user_is_authenticated = 'users:users'
    error_message_user_is_authenticated = (
        user_messages.ERROR_MESSAGE_NOT_RIGHTS
    )
    error_message_not_logged = user_messages.ERROR_MESSAGE_NOT_LOGGED

    def delete(self, request, *args, **kwargs):
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
        object = self.get_object()
        return object.pk == self.request.user.pk
