from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('upload/', views.upload, name='upload'),
    path('csrf/', views.csrf, name='csrf'),
]
