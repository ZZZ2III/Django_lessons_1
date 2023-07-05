from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from app_users.forms import AuthForm, ExtendedRegisterForm, UserExtendedHomework
#from app_users.models import TestUsers
import datetime

from django.views import View


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
                    # print('Ошибка! Нельзя логиниться администраторам')
                    auth_form.add_error('__all__', 'Ошибка! Нельзя логиниться администраторам')

                elif not 8 < datetime.datetime.now().hour < 22:
                    # print('Логиниться можно только с 8-22')
                    auth_form.add_error('__all__', 'Логиниться можно только с 8-22')

                elif user.is_active:
                    login(request, user)
                    # print('Залогинено')
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
    template_name = 'users/logout.html'
    next_page = '/'


def register_view(request):  # не работает
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            print('redirected')
            redirect('/')

    else:
        form = UserCreationForm()
        # print('нихуя')
    return render(request, 'users/register.html', context={'form': form})


def another_register_view(request):  # не работает
    if request.method == 'POST':
        form = ExtendedRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            print('redirected')
            return redirect('/')

    else:
        form = ExtendedRegisterForm()
        # return redirect('/')
    return render(request, 'users/register.html', context={'form': form})


class Register(View):
    def get(self, request):
        form = UserExtendedHomework()
        return render(request, 'users/register.html', context={'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            #TestUsers.objects.create(**form.cleaned_data)
            return redirect('users/account/')


class AccountView(View):
    def get(self,request):
        #form = UserExtendedHomework()
        return render(request, 'users/account.html')#, context={'form': form})
