from django.db import models


class MyUser(models.Model):
    login = models.CharField(max_length=128)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.login


class Messages(models.Model):
    user_name = models.CharField(max_length=128)
    text = models.CharField(max_length=256)
    message_time = models.DateTimeField(auto_now_add=True)
