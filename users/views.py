from django.db import models
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.urls.base import reverse_lazy
from django.views import generic
from django.utils import timezone

from .models import Users, Statuses, Tags, Tasks


class UsersView(generic.ListView):
    model = Users
    # users = Users.objects.all()
    template_name = 'users/users.html'
    # замена имени шаблона вместо дефолтного 'users_list'
    context_object_name = 'all_users_list'
    # замена названия коллекции для html-файла вместо дефолтного object_list
    #!  extra_context = {'title': 'Users'}
    #! # добавление заголовка страницы через атрибут extra_context
    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #     return super().get_context_data(**kwargs)


# class RegisterUser(DataMixin, CreateView):
#     form_class = UserCreationForm
#     template_name = 'users/register.html'
#     success_url = reverse_lazy('login')
#     # https://youtu.be/QK4qbVyY7oU?list=PLA0M1Bcd0w8xO_39zZll2u1lz_Q-Mwn1F

#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title="Registration")
#         return dict(list(context.items()) + list(c_def.items()))


def create(request):
    return HttpResponse('Регистрация пользователя')

def update_user(request, user_id):
    return HttpResponse(f'Редактирование пользователя {user_id}')

def delete_user(request, user_id):
    return HttpResponse(f'Удаление пользователя {user_id}')
