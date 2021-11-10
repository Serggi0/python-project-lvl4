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
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django_tables2 import SingleTableView
from django.contrib.auth.decorators import login_required
from django_filters.views import FilterView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.contrib import messages
from django.shortcuts import redirect

from labels.tables import LabelsTable
from labels.forms import LabelForm
from labels.models import Label
from tasks.models import Task


class LabelsView(LoginRequiredMixin, SingleTableView):
    login_url = 'login'
    model = Label
    table_class = LabelsTable
    template_name = 'labels/labels.html'
    extra_context = {'title': 'Labels'}

    def handle_no_permission(self):
        messages.error(
            self.request,
            _('You are not logged in! Please log in.')
            )
        return redirect(self.login_url)


class CreateLabel(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    login_url = 'login'
    model = Label
    form_class = LabelForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('labels:labels')
    success_message = "%(name)s was created successfully"  # todo Перевод
    extra_context = {
        'title': 'Create Label',
        'button_name': 'Create label'
        }

    def handle_no_permission(self):
        messages.error(
            self.request,
            _('You are not logged in! Please log in.')
            )
        return redirect(self.login_url)

class UpdateLabel(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = 'login'
    model = Label
    form_class = LabelForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('labels:labels')
    success_message = "%(name)s was updated successfully"  # todo Перевод
    extra_context = {'title': 'Update label'}

    def handle_no_permission(self):
        messages.error(
            self.request,
            _('You are not logged in! Please log in.')
            )
        return redirect(self.login_url)


class DeleteLabel(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = 'login'
    model = Label
    form_class = LabelForm
    template_name = 'users/delete.html'
    success_url = reverse_lazy('labels:labels')
    success_message = "Label was deleted successfully"  # todo Перевод
    extra_context = {'title': 'Delete label'}

    def delete(self, request, *args, **kwargs):
        '''
        class DeletionMixin. Вызывается метод delete() и перенаправляется на URL после успешного удаления объекта
        '''
        obj = self.get_object()
        if Task.objects.filter(label=obj.pk):
            messages.error(
                self.request,
                _('It is not possible to delete a label because it is being used')
            )
            return redirect(reverse_lazy('labels'))
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
