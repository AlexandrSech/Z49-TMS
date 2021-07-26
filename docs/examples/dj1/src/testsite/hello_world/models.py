from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    login = models.CharField(max_length=128)
    password = models.CharField(max_length=128)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


class Tasks(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=500)
    task_text = models.TextField()
    task_type = models.IntegerField()
    task_status = models.IntegerField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()
