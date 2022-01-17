from django.urls.base import reverse_lazy
from django.views import generic
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django_tables2 import SingleTableView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.db.models import ProtectedError
from django.utils.translation import gettext as _

from task_manager import user_messages
from statuses.tables import StatusesTable
from statuses.forms import StatusForm
from statuses.models import Status
from task_manager.mixins import HandleNoPermissionMixin


class StatusesView(
    HandleNoPermissionMixin,
    LoginRequiredMixin, SingleTableView
):
    model = Status
    table_class = StatusesTable
    template_name = 'statuses/statuses.html'
    extra_context = {'title': _('Statuses')}
    error_message_not_logged = user_messages.ERROR_MESSAGE_NOT_LOGGED


class CreateStatus(
    HandleNoPermissionMixin,
    LoginRequiredMixin, SuccessMessageMixin,
    generic.CreateView
):
    model = Status
    form_class = StatusForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('statuses:statuses')
    success_message = user_messages.SUCCES_MESSAGE_CREATE_STATUS
    extra_context = {
        'title': _('Create Status'),
        'button_name': _('Create')
    }
    error_message_not_logged = user_messages.ERROR_MESSAGE_NOT_LOGGED


class UpdateStatus(
    HandleNoPermissionMixin,
    LoginRequiredMixin, SuccessMessageMixin,
    UpdateView
):
    model = Status
    form_class = StatusForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('statuses:statuses')
    success_message = user_messages.SUCCES_MESSAGE_UPDATE_STATUS
    extra_context = {'title': _('Update status')}

    error_message_not_logged = user_messages.ERROR_MESSAGE_NOT_LOGGED


class DeleteStatus(
    HandleNoPermissionMixin,
    LoginRequiredMixin, SuccessMessageMixin,
    DeleteView
):
    model = Status
    form_class = StatusForm
    template_name = 'users/delete.html'
    success_url = reverse_lazy('statuses:statuses')
    success_message = user_messages.SUCCES_MESSAGE_DELETE_STATUS
    extra_context = {'title': _('Delete status')}
    error_message_not_logged = user_messages.ERROR_MESSAGE_NOT_LOGGED

    def delete(self, request, *args, **kwargs):
        self.get_object()
        try:
            super(DeleteStatus, self).delete(self.request, *args, **kwargs)
        except ProtectedError:
            messages.error(
                self.request,
                user_messages.ERROR_MESSAGE_NOT_POSSIBLE_DELETE_STATUS,
            )
        else:
            messages.success(
                self.request,
                self.success_message,
            )
        return redirect(self.success_url)
