from django.urls import path, include
from authentication.views import index, registration, message, get_messages


urlpatterns = [
    path('index/', index, name='index'),
    path('registration/', registration, name='registration'),
    path('message/', message, name='message'),
    path('get_messages/', get_messages, name='get_messages'),
]
