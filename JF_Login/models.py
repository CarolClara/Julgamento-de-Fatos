from django.db import models

from JF_Academic.models import Program


class User(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, blank=False, null=False,)
    username = models.CharField(max_length=30, blank=False, null=False, unique=True)
    password = models.CharField(max_lenght=32, blank=False, null=False)
    email = models.EmailField(blank=False, null=False, unique=True)


class Teacher(User):
    pass


class Student(User):

    program = models.ForeignKey(Program, on_delete=models.PROTECT)
