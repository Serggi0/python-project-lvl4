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
from django.views.generic.edit import DeleteView, UpdateView
from django.utils import timezone

from statuses.tables import  StatusesTable
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django_tables2 import SingleTableView
from django.contrib.auth.decorators import login_required
from django_filters.views import FilterView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.contrib import messages
from django.shortcuts import redirect

from statuses.forms import StatusForm
from statuses.models import Status
from tasks.models import Task

class StatusesView(LoginRequiredMixin, SingleTableView):
    login_url = 'login'
    model = Status
    table_class = StatusesTable
    template_name = 'statuses/statuses.html'
    extra_context = {'title': 'Statuses'}

    def handle_no_permission(self):
        messages.error(
            self.request,
            _('You are not logged in! Please log in.')
            )
        return redirect(self.login_url)


class CreateStatus(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    login_url = 'login'
    model = Status
    form_class = StatusForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('statuses:statuses')
    success_message = _("%(name)s was created successfully")  # todo Перевод
    extra_context = {
        'title': 'Create Status',
        'button_name': 'Create'
        }

    def handle_no_permission(self):
        messages.error(
            self.request,
            _('You are not logged in! Please log in.')
            )
        return redirect(self.login_url)


class UpdateStatus(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = 'login'
    model = Status
    form_class = StatusForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('statuses:statuses')
    success_message = _("%(name)s was updated successfully")  # todo Перевод
    extra_context = {'title': 'Update status'}

    def handle_no_permission(self):
        messages.error(
            self.request,
            _('You are not logged in! Please log in.')
            )
        return redirect(self.login_url)


class DeleteStatus(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = 'login'
    model = Status
    form_class = StatusForm
    template_name = 'users/delete.html'
    success_url = reverse_lazy('statuses:statuses')
    success_message = _("Status was deleted successfully")  # todo Перевод
    extra_context = {'title': 'Delete status'}

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        if Task.objects.filter(status=obj.pk):
            messages.error(
                self.request,
                _('It is not possible to delete a status because it is being used')
            )
            return redirect(reverse_lazy('statuses'))
        messages.success(
            self.request,
            self.success_message
            )
        return super().delete(request, *args, **kwargs)

    def handle_no_permission(self):
        messages.error(
            self.request,
            _('You are not logged in! Please log in.')
            )
        return redirect(self.login_url)
