from django.urls import path
from . import views
from .views import AdvertisementListView,AdvertisementDataView

urlpatterns = [
    # path('advertisement_one/', views.advertisement_list, name='advertisement_one'),
    path('advertisement_two/', views.rand_advertisement_list, name='advertisement_two'),
    path('advertisement_three/', views.rand_advertisement_list, name='advertisement_three'),
    path('advertisement_four/', views.rand_advertisement_list, name='advertisement_four'),
    path('advertisement_five/', views.rand_advertisement_list, name='advertisement_five'),
    path('user_info/', views.user_ip, name='user_info'),
    path('base_advertis/', views.base_adverisement, name='base_advertisement'),
    path('advertisement/', views.homepage, name='homepage'),
    path('about/', views.About.as_view(), name='About'),
    path('regions/', views.Regions.as_view(), name='regions'),
    path('advertisements/', views.Counter.as_view(), name='advertisements'),
    path('contacts/', views.Templ.as_view(), name='contacts'),
    path('mod_adv/', views.advertisement_list, name='free_advertisements'),
    path('test/', views.testing, name='mytest'),
    path('advertisement_list/', AdvertisementListView.as_view(), name='advertisement'),
    path('advertisement_list/<int:pk>', AdvertisementDataView.as_view(), name='advertisement-detail')

]
