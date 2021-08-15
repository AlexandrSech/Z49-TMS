from django.urls import path
from users.views import users_list, profile, my_login, get_token, get_list


urlpatterns = [
    path('login', my_login, name='login'),
    path('get_token', get_token, name='get_token'),
    path('get_list', get_list, name='get_list'),
    path('users_list', users_list, name='users_list'),
    path('profile/<int:user_id>/', profile, name='profile'),
]
