from django.contrib.auth.views import LoginView
from django.db import models
from django.db.models import fields
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.urls.base import reverse_lazy
from django.views import generic
from django.views.generic.edit import DeleteView, UpdateView
from django.utils import timezone
from users.forms import CreateStatusForm, CreateUserForm, UpdateStatusForm, UpdateUserForm
from users.tables import StatusesTable, UsersTable

from .models import User, Statuses, Tags, Tasks
from django_tables2 import SingleTableView
# from django.contrib.auth.models import User


from django.contrib.messages.views import SuccessMessageMixin

class UsersView(SingleTableView):
    model = User
    # users = Users.objects.all()
    table_class = UsersTable
    template_name = 'users/users.html'
    # замена имени шаблона вместо дефолтного 'users_list'
    # context_object_name = 'all_users_list'
    # замена названия коллекции для html-файла вместо дефолтного object_list
    extra_context = {'title': 'Users'}
    #! # добавление заголовка страницы через атрибут extra_context
    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #     return super().get_context_data(**kwargs)


class StatusesView(SingleTableView):
    model = Statuses
    table_class = StatusesTable
    template_name = 'users/statuses.html'
    # замена имени шаблона вместо дефолтного 'users_list'
    # context_object_name = 'statuses_list'
    # замена названия коллекции для html-файла вместо дефолтного object_list
    extra_context = {'title': 'Statuses'}


class CreateUser(SuccessMessageMixin, generic.CreateView):
    form_class = CreateUserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')
    # https://youtu.be/QK4qbVyY7oU?list=PLA0M1Bcd0w8xO_39zZll2u1lz_Q-Mwn1F
    success_message = "%(username)s was created successfully"  # todo Перевод
    # ! https://djangodoc.ru/3.1/ref/contrib/messages/
    extra_context = {'title': 'Registration'}

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     c_def = self.get_user_context(title="Registration")
    #     return dict(list(context.items()) + list(c_def.items()))


class UpdateUser(UpdateView):
    model = User
    # fields = ['username', 'first_name', 'last_name', 'password']
    form_class = UpdateUserForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('login')
    extra_context = {'title': 'Update'}

# def create(request):
#     return HttpResponse('Регистрация пользователя')

# def update_user(request, user_id):
#     return HttpResponse(f'Редактирование пользователя {user_id}')

# def delete_user(request, user_id):
#     u = Users.objects.get(pk=user_id)
#     u.delete()
#     return HttpResponse(f'Удаление пользователя {user_id}')

class DeleteUser(DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users')
    extra_context = {'title': 'Delete'}


class CreateStatus(SuccessMessageMixin, generic.CreateView):
    # model = Statuses
    form_class = CreateStatusForm
    # fields = ['name']
    template_name = 'users/create-status.html'
    success_url = reverse_lazy('statuses')
    success_message = "%(name)s was created successfully"  # todo Перевод
    extra_context = {'title': 'Create Status'}

class DeleteStatus(DeleteView):
    model = Statuses
    template_name = 'users/delete.html'
    success_url = reverse_lazy('statuses')
    extra_context = {'title': 'Delete'}


class UpdateStatus(UpdateView):
    model = Statuses
    form_class = UpdateStatusForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('statuses')
    extra_context = {'title': 'Update'}