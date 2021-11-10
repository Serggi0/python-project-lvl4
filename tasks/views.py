from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.db import models
from django.db.models import fields
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.urls.base import reverse_lazy
from django.views import generic
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django_tables2 import SingleTableView
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django_filters.views import FilterView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.

from tasks.models import Task
from tasks.filters import TaskFilter
from tasks.forms import TaskForm, DeleteTaskForm
from tasks.tables import TasksTable


class TasksView(LoginRequiredMixin, FilterView, SingleTableView):
    login_url = 'login'
    model = Task
    filterset_class = TaskFilter
    table_class = TasksTable
    template_name = 'tasks/tasks.html'
    extra_context = {'title': 'Tasks'}

    def handle_no_permission(self):
        messages.error(
            self.request,
            _('You are not logged in! Please log in.')
            )
        return redirect(self.login_url)



class CreateTask(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    login_url = 'login'
    model = Task
    form_class = TaskForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('tasks:tasks')
    success_message = "%(name)s was created successfully"  # todo Перевод
    extra_context = {
        'title': 'Create task',
        'button_name': 'Create'
        }

    def form_valid(self, form):
        '''
        Чтобы отслеживать, с помощью какого пользователя был создан CreateTask (объект CreateView)
        '''
        form.instance.author = self.request.user
        return super().form_valid(form)

    def handle_no_permission(self):
        '''
        Перенаправление на страницу login, вместо исключения PermissionDenied
        '''
        messages.error(
            self.request,
            _('You are not logged in! Please log in.')
            )
        return redirect(self.login_url)


class UpdateTask(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = 'login'
    model = Task
    form_class = TaskForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('tasks:tasks')
    success_message = "%(name)s was updated successfully"  # todo Перевод
    extra_context = {'title': 'Update task'}

    def handle_no_permission(self):
        messages.error(
            self.request,
            _('You are not logged in! Please log in.')
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
            _('You are not logged in! Please log in.')
            )
        return redirect(self.login_url)


class DeleteTask(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = 'login'
    model = Task
    form_class = DeleteTaskForm
    template_name = 'users/delete.html'
    success_url = reverse_lazy('tasks:tasks')
    success_message = "Task was deleted successfully"  # todo Перевод
    extra_context = {'title': 'Delete task'}


    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request,
            self.success_message
            )
        return super().delete(request, *args, **kwargs)

    def test_func(self):
        obj = self.get_object()
        if self.request.user.is_authenticated and obj.pk != self.request.user.pk:
            self.error_message = _("A task can only be deleted by its author")
            self.login_url = reverse_lazy('tasks:tasks')
            return False
        return True


    def handle_no_permission(self):
        messages.error(
            self.request,
            _('You are not logged in! Please log in.')
            )
        return redirect(self.login_url)