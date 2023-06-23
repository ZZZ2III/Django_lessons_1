from django.urls import path
from . import views
from news.views import NewsFromView, CommetFormView, SortedNews, All_news

urlpatterns = [
    path('makenew/', NewsFromView.as_view(), name='Создание новости'),
    path('makecomm/', CommetFormView.as_view(), name='Создание комментария'),
    path('allnews/', SortedNews.as_view(), name='Просмотр страниц'),
    path('news_list/', All_news.as_view(), name='Список всех новостей на сегодня'),
    path('news_list/<int:pk>', SortedNews.as_view(), name='Новости каждая -detail'),
]
