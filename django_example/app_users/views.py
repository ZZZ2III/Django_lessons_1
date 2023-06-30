from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView,LogoutView
from django.http import HttpResponse
from django.shortcuts import render
from app_users.forms import AuthForm
import datetime


# Create your views here.
def login_view(request):
    if request.method == 'POST':  # Для пост пытаемся аутентифицировать пользователя
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_superuser:
                    #print('Ошибка! Нельзя логиниться администраторам')
                    auth_form.add_error('__all__', 'Ошибка! Нельзя логиниться администраторам')

                elif not 8 < datetime.datetime.now().hour < 22:
                    #print('Логиниться можно только с 8-22')
                    auth_form.add_error('__all__', 'Логиниться можно только с 8-22')

                elif user.is_active:
                    login(request, user)
                    #print('Залогинено')
                    return HttpResponse('Вы успешно вошли в систему')
                else:
                    auth_form.add_error('__all__', 'Ошибка! Учетная запись не активна')

            else:
                auth_form.add_error('__all__', 'Ошибка! Проверьте правильность написания логина или пароля')

    else:  # Для всех остальных запросов отображаем страницу
        auth_form = AuthForm()
    context = {'form': auth_form}
    return render(request, 'users/login.html', context=context)

class AnotherLoginView(LoginView):
    template_name = 'users/login.html'



def logout_view(request):
    logout(request)
    return HttpResponse('Вы вышли из под своей учетной записи')


class AnotherLogoutView(LogoutView):
    #template_name = 'users/logout.html'
    next_page = '/'