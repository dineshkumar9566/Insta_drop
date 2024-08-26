from django.urls import path
from .views import download_post , download_video , download_story, home

urlpatterns = [
    path('', home, name='home'),
    path('download/post', download_post, name='download_post'),
    path('download/video', download_video, name='download_video'),
    path('download/story', download_story, name='download_story'),
]