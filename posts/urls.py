from django.urls import URLPattern, path 
from django.contrib import admin
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:post_id>/', views.delete, name='delete'),
    path('edit/<int:post_id>/', views.edit, name='edit'),
    path('like/<int:post_id>/', views.likes, name='like'),
]
 