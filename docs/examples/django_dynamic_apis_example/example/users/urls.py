from django.urls import path
from users.views import users_list, profile


urlpatterns = [
    path('users_list', users_list, name='users_list'),
    path('profile/<int:user_id>/', profile, name='profile'),
]
