from django.urls import path

from . import views

urlpatterns = [
    path('api/v1/reset/', views.reset, name='reset'),
    path('api/v1/', views.index, name='index'),
]
