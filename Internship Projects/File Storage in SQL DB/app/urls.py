from django.urls import path
from .views import upload_file, file_list, download_file

urlpatterns = [
    path('upload/', upload_file, name='upload_file'),
    path('', file_list, name='file_list'),
    path('files/<str:file_number>/', download_file, name='download_file'),
]
