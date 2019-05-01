from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField(max_length=250)
    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Teacher(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name


class Student(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    program = models.ForeignKey('academic.Program', on_delete=models.PROTECT)

    def __str__(self):
        return self.user.name
