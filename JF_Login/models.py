from django.db import models


class User(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=32)
    email = models.EmailField(unique=True)


class Teacher(User):
    pass


class Student(User):

    program = models.ForeignKey('JF_Academic.Program', on_delete=models.PROTECT)
