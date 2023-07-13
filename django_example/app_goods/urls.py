from django.urls import path
from app_goods.views import item_list, update_prices, goods_list, update_goods, goods_list_hw, update_goods_with_saving

urlpatterns = [
    path('items/', item_list, name='item_list'),
    path('update_prices/', update_prices, name='update_prices'),
    path('goods/', goods_list, name='goods'),
    path('update_goods/', update_goods, name='update_goods'),
    path('view_hw/', goods_list_hw, name='view_hw'),
    path('updated_view_hw/', update_goods_with_saving, name='update_view_hw'),
]
