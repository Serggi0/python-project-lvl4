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
from users.filters import TaskFilter
from users.forms import CreateLabelForm, CreateStatusForm, CreateTaskForm, CreateUserForm, DeleteLabelForm, DeleteStatusForm, DeleteTaskForm, UpdateLabelForm, UpdateStatusForm, UpdateTaskForm, UpdateUserForm
from users.tables import LabelsTable, StatusesTable, TasksTable, UsersTable
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import User, Status, Label, Task
from django_tables2 import SingleTableView
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django_filters.views import FilterView
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


class CreateUser(SuccessMessageMixin, generic.CreateView):
    form_class = CreateUserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')
    # https://youtu.be/QK4qbVyY7oU?list=PLA0M1Bcd0w8xO_39zZll2u1lz_Q-Mwn1F
    success_message = "%(username)s was created successfully"  # todo Перевод
    # ! https://djangodoc.ru/3.1/ref/contrib/messages/
    extra_context = {
        'title': 'Registration',
        'button_name': 'Register'
        }

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     c_def = self.get_user_context(title="Registration")
    #     return dict(list(context.items()) + list(c_def.items()))


class UpdateUser(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = User
    # fields = ['username', 'first_name', 'last_name', 'password']
    form_class = UpdateUserForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('login')
    extra_context = {'title': 'Update user'}

# def create(request):
#     return HttpResponse('Регистрация пользователя')

# def update_user(request, user_id):
#     return HttpResponse(f'Редактирование пользователя {user_id}')

# def delete_user(request, user_id):
#     u = Users.objects.get(pk=user_id)
#     u.delete()
#     return HttpResponse(f'Удаление пользователя {user_id}')


class DeleteUser(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users')
    extra_context = {'title': 'Delete user'}


class StatusesView(LoginRequiredMixin, SingleTableView):
    login_url = 'login'
    model = Status
    table_class = StatusesTable
    template_name = 'users/statuses.html'
    # замена имени шаблона вместо дефолтного 'users_list'
    # context_object_name = 'statuses_list'
    # замена названия коллекции для html-файла вместо дефолтного object_list
    extra_context = {'title': 'Statuses'}


class CreateStatus(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    login_url = 'login'
    model = Status
    form_class = CreateStatusForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('users:statuses')
    success_message = "%(name)s was created successfully"  # todo Перевод
    extra_context = {
        'title': 'Create Status',
        'button_name': 'Create'
        }


class DeleteStatus(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = 'login'
    model = Status
    form_class = DeleteStatusForm
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users:statuses')
    success_message = "%(name)s was deleted successfully"  # todo Перевод
    extra_context = {'title': 'Delete status'}


class UpdateStatus(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = 'login'
    model = Status
    form_class = UpdateStatusForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users:statuses')
    success_message = "%(name)s was updated successfully"  # todo Перевод
    extra_context = {'title': 'Update status'}


class TasksView(LoginRequiredMixin, FilterView, SingleTableView):
    login_url = 'login'
    model = Task
    filterset_class = TaskFilter
    table_class = TasksTable
    template_name = 'users/tasks.html'
    extra_context = {'title': 'Tasks'}


class CreateTask(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    login_url = 'login'
    model = Task
    form_class = CreateTaskForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('users:tasks')
    success_message = "%(name)s was created successfully"  # todo Перевод
    extra_context = {
        'title': 'Create task',
        'button_name': 'Create'
        }


class DeleteTask(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = 'login'
    model = Task
    form_class = DeleteTaskForm
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users:tasks')
    success_message = "%(name)s was deleted successfully"  # todo Перевод
    extra_context = {'title': 'Delete task'}


class UpdateTask(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = 'login'
    model = Task
    form_class = UpdateTaskForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users:tasks')
    success_message = "%(name)s was updated successfully"  # todo Перевод
    extra_context = {'title': 'Update task'}


class LabelsView(LoginRequiredMixin, SingleTableView):
    login_url = 'login'
    model = Label
    table_class = LabelsTable
    template_name = 'users/labels.html'
    # замена имени шаблона вместо дефолтного 'users_list'
    # context_object_name = 'statuses_list'
    # замена названия коллекции для html-файла вместо дефолтного object_list
    extra_context = {'title': 'Labels'}


class CreateLabel(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    login_url = 'login'
    model = Label
    form_class = CreateLabelForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('users:labels')
    success_message = "%(name)s was created successfully"  # todo Перевод
    extra_context = {
        'title': 'Create Label',
        'button_name': 'Create label'
        }


class DeleteLabel(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = 'login'
    model = Label
    form_class = DeleteLabelForm
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users:labels')
    success_message = "%(name)s was deleted successfully"  # todo Перевод
    extra_context = {'title': 'Delete label'}


class UpdateLabel(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = 'login'
    model = Label
    form_class = UpdateLabelForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users:labels')
    success_message = "%(name)s was updated successfully"  # todo Перевод
    extra_context = {'title': 'Update label'}
