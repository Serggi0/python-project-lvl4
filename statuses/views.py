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
from tasks.models import Task


class StatusesView(LoginRequiredMixin, SingleTableView):
    login_url = 'login'
    model = Status
    table_class = StatusesTable
    template_name = 'statuses/statuses.html'
    extra_context = {'title': _('Statuses')}

    def handle_no_permission(self):
        messages.error(
            self.request,
            user_messages.ERROR_MESSAGE_NOT_LOGGED
        )
        return redirect(self.login_url)


class CreateStatus(
    LoginRequiredMixin, SuccessMessageMixin, generic.CreateView
):
    login_url = 'login'
    model = Status
    form_class = StatusForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('statuses:statuses')
    success_message = user_messages.SUCCES_MESSAGE_CREATE_STATUS
    extra_context = {
        'title': _('Create Status'),
        'button_name': _('Create')
    }

    def handle_no_permission(self):
        messages.error(
            self.request,
            user_messages.ERROR_MESSAGE_NOT_LOGGED
        )
        return redirect(self.login_url)


class UpdateStatus(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = 'login'
    model = Status
    form_class = StatusForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('statuses:statuses')
    success_message = user_messages.SUCCES_MESSAGE_UPDATE_STATUS
    extra_context = {'title': _('Update status')}

    def handle_no_permission(self):
        messages.error(
            self.request,
            user_messages.ERROR_MESSAGE_NOT_LOGGED
        )
        return redirect(self.login_url)


class DeleteStatus(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = 'login'
    model = Status
    form_class = StatusForm
    template_name = 'users/delete.html'
    success_url = reverse_lazy('statuses:statuses')
    success_message = user_messages.SUCCES_MESSAGE_DELETE_STATUS
    extra_context = {'title': _('Delete status')}

    def delete(self, request, *args, **kwargs):
        '''
        Вызывается метод delete()
        и перенаправляется на URL после успешного удаления объекта
        '''
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

    def handle_no_permission(self):
        messages.error(
            self.request,
            user_messages.ERROR_MESSAGE_NOT_LOGGED
        )
        return redirect(self.login_url)
