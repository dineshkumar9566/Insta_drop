from django.urls import path
from .views import download_post , download_vedio , download_story

urlpatterns = [
    path('download/post', download_post, name='download_post'),
    path('download/vedio', download_vedio, name='download_vedio'),
    path('download/story', download_story, name='download_story'),
]