from django.urls import path
from . import views

urlpatterns = [
    path('advertisement_one/', views.advertisement_list, name='advertisement_one'),
    path('advertisement_two/', views.rand_advertisement_list, name='advertisement_two'),
    path('advertisement_three/', views.rand_advertisement_list, name='advertisement_three'),
    path('advertisement_four/', views.rand_advertisement_list, name='advertisement_four'),
    path('advertisement_five/', views.rand_advertisement_list, name='advertisement_five'),
    path('user_info/', views.user_ip, name='user_info'),
    path('base_advertis/', views.base_adverisement, name='base_advertisement'),
    path('', views.homepage, name='homepage'),
    path('about/', views.About.as_view(), name='About'),
    path('regions/', views.Regions.as_view(), name='regions'),
    path('advertisements/', views.Counter.as_view(), name='advertisements'),
    path('contacts/', views.Templ.as_view(),name ='contacts')

]
