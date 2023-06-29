from django.contrib import admin
from django.urls import path,include
from app_users.views import login_view,AnotherLoginView


urlpatterns =[
    path('login/', login_view, name = 'login'),
    path('anotherlogin/',AnotherLoginView.as_view(),name ='another_login')
]