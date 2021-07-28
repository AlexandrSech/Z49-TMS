from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('task_19_1/', views.task_19_1, name='base_form'),
    path('task_19_2/', views.task_19_2, name='task_19_2'),


]
