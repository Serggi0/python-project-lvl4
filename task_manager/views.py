from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import logout


def index(request):
    return render(request, 'home.html', context={
        'title': 'Task manager',
    })

def login(request):
    return HttpResponse('Авторизация')


def logout(request, user_id):
    # разлогинивание
    logout(request, user_id)
    return redirect('home')
