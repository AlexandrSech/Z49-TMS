from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.main, name="main"),
    path('main/', views.main, name="main"),
    path('detail/<int:user_id>', views.detail, name="detail"),
    path('delete/', views.delete, name="delete"),

]
