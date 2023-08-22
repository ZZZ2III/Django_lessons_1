from django.urls import path
from app_pages.views import translation_example, translation_homework, welcome, main_page
from django.views.decorators.cache import cache_page
urlpatterns = [
    path('example/', translation_example, name='example'),
    path('homework/', translation_homework, name='homework'),
    path('welcome/', welcome, name='welcome'),
    path('main_page/', main_page, name='main_page')
]
