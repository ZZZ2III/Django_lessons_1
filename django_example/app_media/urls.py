from django.urls import path
from app_media.views import UploadFile, UploadFileHomework, UploadFileToFolder

urlpatterns = [
    path('uploadfile/', UploadFile, name='upload_file'),
    path('uploadfile2/', UploadFileHomework, name='upload_file2'),
    path('save/', UploadFileToFolder, name='save_to_file'),
]
