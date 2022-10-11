from django.shortcuts import render


def login(request):
    return render(request, 'users/login_form.html', {'title': 'Авторизация', 'description': 'Форма авторизации'})
