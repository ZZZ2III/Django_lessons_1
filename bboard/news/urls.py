from django.urls import path
from . import views
from news.views import NewsFromView, CommetFormView, SortedNews, All_news, NewsLoginView, NewsLogoutView

urlpatterns = [
    path('makenew/', NewsFromView.as_view(), name='news_creation'),
    path('makecomm/', CommetFormView.as_view(), name='comms_creation'),
    path('news_list/', All_news.as_view(), name='all_news'),
    path('news_list/<int:pk>', SortedNews.as_view(), name='Новости каждая -detail'),
    path('login/', NewsLoginView.as_view(), name='login'),
    path('logout/', NewsLogoutView.as_view(), name='logout'),

]
