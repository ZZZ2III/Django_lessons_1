from django.urls import path
from app_media.views import UploadFile,UploadFileHomework
urlpatterns = [
    path('uploadfile/', UploadFile,name = 'upload_file'),
    path('uploadfile2/', UploadFileHomework,name = 'upload_file2'),
]