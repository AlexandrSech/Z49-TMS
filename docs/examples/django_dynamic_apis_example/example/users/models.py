from django.db import models


class Users(models.Model):
    login = models.CharField(max_length=128)
    password = models.CharField(max_length=128)


class Profile(models.Model):
    user_id = models.IntegerField()
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    age = models.IntegerField()
