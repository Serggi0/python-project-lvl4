from django.urls.base import reverse_lazy
from django.views import generic
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django_tables2 import SingleTableView

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _

from task_manager import user_messages
from labels.tables import LabelsTable
from labels.forms import LabelForm
from labels.models import Label
from tasks.models import Task


class LabelsView(LoginRequiredMixin, SingleTableView):
    login_url = 'login'
    model = Label
    table_class = LabelsTable
    template_name = 'labels/labels.html'
    extra_context = {'title': _('Labels')}

    def handle_no_permission(self):
        messages.error(
            self.request,
            user_messages.ERROR_MESSAGE_NOT_LOGGED
        )
        return redirect(self.login_url)


class CreateLabel(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    login_url = 'login'
    model = Label
    form_class = LabelForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('labels:labels')
    success_message = user_messages.SUCCES_MESSAGE_CREATE_LABEL
    extra_context = {
        'title': _('Create Label'),
        'button_name': _('Create')
    }

    def handle_no_permission(self):
        messages.error(
            self.request,
            user_messages.ERROR_MESSAGE_NOT_LOGGED
        )
        return redirect(self.login_url)


class UpdateLabel(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = 'login'
    model = Label
    form_class = LabelForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('labels:labels')
    success_message = user_messages.SUCCES_MESSAGE_UPDATE_LABEL
    extra_context = {'title': _('Update label')}

    def handle_no_permission(self):
        messages.error(
            self.request,
            user_messages.ERROR_MESSAGE_NOT_LOGGED
        )
        return redirect(self.login_url)


class DeleteLabel(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = 'login'
    model = Label
    form_class = LabelForm
    template_name = 'users/delete.html'
    success_url = reverse_lazy('labels:labels')
    success_message = user_messages.SUCCES_MESSAGE_DELETE_LABEL
    extra_context = {'title': _('Delete label')}

    def delete(self, request, *args, **kwargs):
        '''
        class DeletionMixin. Вызывается метод delete()
        и перенаправляется на URL после успешного удаления объекта
        '''
        object = self.get_object()
        if Task.objects.filter(label=object.pk):
            messages.error(
                self.request,
                user_messages.ERROR_MESSAGE_NOT_POSSIBLE_DELETE_LABEL
            )
            return redirect(reverse_lazy('labels:labels'))
        messages.success(
            self.request,
            self.success_message
        )
        return super().delete(request, *args, **kwargs)

    def handle_no_permission(self):
        messages.error(
            self.request,
            user_messages.ERROR_MESSAGE_NOT_LOGGED
        )
        return redirect(self.login_url)
