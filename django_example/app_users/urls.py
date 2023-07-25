from django.contrib import admin
from django.urls import path, include
from app_users.views import login_view, AnotherLoginView, logout_view, AnotherLogoutView, register_view, \
    another_register_view,Register,restore_password

from app_users.views import AccountView

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('anotherlogin/', AnotherLoginView.as_view(), name='another_login'),
    path('another_logout/', AnotherLogoutView.as_view(), name='another_logout'),
    path('register/', register_view, name='register'),
    path('new_register/', another_register_view, name='new_register'),
    path('bd_register/', Register.as_view(),name ='homework_register'),
    path('account/', AccountView.as_view(),name ='account'),
    path('restore_password',restore_password,name = 'restore_password')
]
