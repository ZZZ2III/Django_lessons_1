from django.urls import path
from app_goods.views import items_list, items_list_groups, ItemList

urlpatterns = [
    path('items/', items_list, name='items_list'),
    path('groups/', items_list_groups, name='groups'),
    path('items_class/', ItemList.as_view(), name='items_class')
]
