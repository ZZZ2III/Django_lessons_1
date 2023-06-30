from django.contrib import admin
from django.urls import path,include
from app_users.views import login_view,AnotherLoginView,logout_view,AnotherLogoutView


urlpatterns =[
    path('login/', login_view, name = 'login'),
    path('logout/',logout_view,name ='logout'),
    path('anotherlogin/',AnotherLoginView.as_view(),name ='another_login'),
    path('another_logout',AnotherLogoutView.as_view(), name ='another_logout')

]