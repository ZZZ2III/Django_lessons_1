from django.urls import path
from app_pages.views import translation_example, translation_homework

urlpatterns = [
    path('example/', translation_example, name='example'),
    path('homework/', translation_homework, name='homework'),
]
