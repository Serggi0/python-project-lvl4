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

from task_manager import user_messages
from tasks.models import Task
from tasks.filters import TaskFilter
from tasks.forms import TaskForm
from tasks.tables import TasksTable


class TasksView(LoginRequiredMixin, FilterView, SingleTableView):
    login_url = 'login'
    model = Task
    filterset_class = TaskFilter
    table_class = TasksTable
    template_name = 'tasks/tasks.html'
    extra_context = {'title': 'Tasks'}

    def handle_no_permission(self):
        '''
        Перенаправление на страницу login, вместо исключения PermissionDenied
        '''
        messages.error(
            self.request,
            user_messages.ERROR_MESSAGE_NOT_LOGGED
        )
        return redirect(self.login_url)


class CreateTask(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    login_url = 'login'
    model = Task
    form_class = TaskForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('tasks:tasks')
    success_message = user_messages.SUCCES_MESSAGE_CREATE_TASK
    extra_context = {
        'title': 'Create task',
        'button_name': 'Create'
    }

    def form_valid(self, form):
        '''
        Чтобы отслеживать, с помощью какого пользователя
        был создан CreateTask (объект CreateView)
        '''
        form.instance.author = self.request.user
        return super().form_valid(form)

    def handle_no_permission(self):
        messages.error(
            self.request,
            user_messages.ERROR_MESSAGE_NOT_LOGGED
        )
        return redirect(self.login_url)


class UpdateTask(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = 'login'
    model = Task
    form_class = TaskForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('tasks:tasks')
    success_message = user_messages.SUCCES_MESSAGE_UPDATE_TASK
    extra_context = {'title': 'Update task'}

    def handle_no_permission(self):
        messages.error(
            self.request,
            user_messages.ERROR_MESSAGE_NOT_LOGGED
        )
        return redirect(self.login_url)


class TaskView(LoginRequiredMixin, SuccessMessageMixin, DetailView):
    login_url = 'login'
    model = Task
    template_name = 'tasks/view_task.html'
    extra_context = {'title': 'View task'}

    def handle_no_permission(self):
        messages.error(
            self.request,
            user_messages.ERROR_MESSAGE_NOT_LOGGED
        )
        return redirect(self.login_url)


class DeleteTask(
    LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, DeleteView
):
    login_url = 'login'
    model = Task
    template_name = 'users/delete.html'
    success_url = reverse_lazy('tasks:tasks')
    success_message = user_messages.SUCCES_MESSAGE_DELETE_TASK
    error_message = user_messages.ERROR_MESSAGE_NOT_LOGGED
    extra_context = {'title': 'Delete task'}

    def handle_no_permission(self):
        messages.error(
            self.request,
            self.error_message
        )
        return redirect(self.login_url)

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
