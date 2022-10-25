from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def login(request):
    return render(request, 'users/login.html', {'title': 'Авторизация', 'description': 'Форма авторизации'})


def registration(request):
    form = UserCreationForm()
    return render(request, 'users/registration.html',
                  {'title': 'Регистрация', 'description': 'Форма регистрации', 'form': form})
