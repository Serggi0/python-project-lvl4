from django.urls.base import reverse_lazy
from django.views import generic
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django_tables2 import SingleTableView
from django_filters.views import FilterView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.utils.translation import gettext as _

from users.models import User
from task_manager import user_messages
from tasks.models import Task
from tasks.filters import TaskFilter
from tasks.forms import TaskForm
from tasks.tables import TasksTable
from task_manager.utils import HandleNoPermissionMixin


class TasksView(
    HandleNoPermissionMixin,
    LoginRequiredMixin, FilterView,
    SingleTableView
):
    model = Task
    filterset_class = TaskFilter
    table_class = TasksTable
    template_name = 'tasks/tasks.html'
    extra_context = {'title': _('Tasks')}
    url_if_user_is_authenticated = 'tasks:tasks'
    error_message_user_is_authenticated = (
        user_messages.ERROR_MESSAGE_DELETED_TASK
    )
    error_message_not_logged = user_messages.ERROR_MESSAGE_NOT_LOGGED


class CreateTask(
    HandleNoPermissionMixin,
    LoginRequiredMixin, SuccessMessageMixin,
    generic.CreateView
):
    model = Task
    form_class = TaskForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('tasks:tasks')
    success_message = user_messages.SUCCES_MESSAGE_CREATE_TASK
    extra_context = {
        'title': 'Create task',
        'button_name': _('Create')
    }
    url_if_user_is_authenticated = 'tasks:tasks'
    error_message_user_is_authenticated = (
        user_messages.ERROR_MESSAGE_DELETED_TASK
    )
    error_message_not_logged = user_messages.ERROR_MESSAGE_NOT_LOGGED

    def form_valid(self, form):
        form.instance.author = User.objects.get(pk=self.request.user.pk)
        return super().form_valid(form)


class UpdateTask(
    HandleNoPermissionMixin,
    LoginRequiredMixin, SuccessMessageMixin,
    UpdateView
):
    model = Task
    form_class = TaskForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('tasks:tasks')
    success_message = user_messages.SUCCES_MESSAGE_UPDATE_TASK
    extra_context = {'title': _('Update task')}
    url_if_user_is_authenticated = 'tasks:tasks'
    error_message_user_is_authenticated = (
        user_messages.ERROR_MESSAGE_DELETED_TASK
    )
    error_message_not_logged = user_messages.ERROR_MESSAGE_NOT_LOGGED


class TaskView(
    HandleNoPermissionMixin,
    LoginRequiredMixin, SuccessMessageMixin,
    DetailView
):
    model = Task
    template_name = 'tasks/view_task.html'
    extra_context = {'title': _('Tasks')}
    url_if_user_is_authenticated = 'tasks:tasks'
    error_message_user_is_authenticated = (
        user_messages.ERROR_MESSAGE_DELETED_TASK
    )
    error_message_not_logged = user_messages.ERROR_MESSAGE_NOT_LOGGED


class DeleteTask(
    HandleNoPermissionMixin,
    LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin,
    DeleteView
):
    model = Task
    template_name = 'users/delete.html'
    success_url = reverse_lazy('tasks:tasks')
    success_message = user_messages.SUCCES_MESSAGE_DELETE_TASK
    extra_context = {'title': _('Delete task')}
    url_if_user_is_authenticated = 'tasks:tasks'
    error_message_user_is_authenticated = (
        user_messages.ERROR_MESSAGE_DELETED_TASK
    )
    error_message_not_logged = user_messages.ERROR_MESSAGE_NOT_LOGGED

    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request,
            self.success_message
        )
        return super().delete(request, *args, **kwargs)

    def test_func(self):
        object = self.get_object()
        return object.author.pk == self.request.user.pk
