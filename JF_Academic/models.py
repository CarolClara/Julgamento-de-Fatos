from django.db import models

from JF_Login.models import Student


class Class(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    student = models.ManyToManyField(Student)


class Course(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    course = models.ManyToManyField(Class)


class Program(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    course = models.ManyToManyField(Course)


class Unit(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    program = models.ManyToManyField(Program)
