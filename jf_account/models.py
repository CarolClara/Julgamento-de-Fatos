from django.db import models


class User(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=32)
    email = models.EmailField(unique=True)


class Teacher(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Student(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    program = models.ForeignKey('jf_academic.Program', on_delete=models.PROTECT)
