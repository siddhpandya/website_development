from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_media, name='upload_media'),
    path('upload/success/', views.upload_success, name='upload_success'),
    path('media/', views.media_list, name='media_list'),
]
