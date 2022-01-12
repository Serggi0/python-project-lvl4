from django.urls.base import reverse_lazy
from django.views import generic
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django_tables2 import SingleTableView
from django_filters.views import FilterView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _

from users.models import User
from task_manager import user_messages
from tasks.models import Task
from tasks.filters import TaskFilter
from tasks.forms import TaskForm
from tasks.tables import TasksTable


class HandleNoPermission():
    def not_permit(self):
        messages.error(
            self.request,
            user_messages.ERROR_MESSAGE_NOT_LOGGED
        )
        return redirect(self.login_url)


class TasksView(
    LoginRequiredMixin, FilterView,
    SingleTableView, HandleNoPermission
):
    login_url = 'login'
    model = Task
    filterset_class = TaskFilter
    table_class = TasksTable
    template_name = 'tasks/tasks.html'
    extra_context = {'title': _('Tasks')}

    def handle_no_permission(self):
        return super().not_permit()


class CreateTask(
    LoginRequiredMixin, SuccessMessageMixin,
    generic.CreateView, HandleNoPermission
):
    login_url = 'login'
    model = Task
    form_class = TaskForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('tasks:tasks')
    success_message = user_messages.SUCCES_MESSAGE_CREATE_TASK
    extra_context = {
        'title': 'Create task',
        'button_name': _('Create')
    }

    def form_valid(self, form):
        form.instance.author = User.objects.get(pk=self.request.user.pk)
        return super().form_valid(form)

    def handle_no_permission(self):
        return super().not_permit()


class UpdateTask(
    LoginRequiredMixin, SuccessMessageMixin,
    UpdateView, HandleNoPermission
):
    login_url = 'login'
    model = Task
    form_class = TaskForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('tasks:tasks')
    success_message = user_messages.SUCCES_MESSAGE_UPDATE_TASK
    extra_context = {'title': _('Update task')}

    def handle_no_permission(self):
        return super().not_permit()


class TaskView(
    LoginRequiredMixin, SuccessMessageMixin,
    DetailView, HandleNoPermission
):
    login_url = 'login'
    model = Task
    template_name = 'tasks/view_task.html'
    extra_context = {'title': _('Tasks')}

    def handle_no_permission(self):
        return super().not_permit()


class DeleteTask(
    LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin,
    DeleteView, HandleNoPermission
):
    login_url = 'login'
    model = Task
    template_name = 'users/delete.html'
    success_url = reverse_lazy('tasks:tasks')
    success_message = user_messages.SUCCES_MESSAGE_DELETE_TASK
    extra_context = {'title': _('Delete task')}

    def handle_no_permission(self):
        return super().not_permit()

    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request,
            self.success_message
        )
        return super().delete(request, *args, **kwargs)

    def test_func(self):
        self.object = self.get_object()

        if self.object.author.pk == self.request.user.pk:
            return True
        else:
            self.error_message = user_messages.ERROR_MESSAGE_DELETED_TASK
            self.login_url = reverse_lazy('tasks:tasks')
            return False
