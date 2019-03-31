from django.db import models

from JF_Login.models import Student


class Class(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField()
    student = models.ManyToManyField(Student)


class ClassStudent(models.Model):

    id = models.AutoField(primary_key=True)
    class_id = models.ForeignKey(Class.id, on_delete=models.PROTECT)
    student_id = models.ForeignKey(Student.id, on_delete=models.PROTECT)


class Course(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField()
    course = models.ManyToManyField(Class)


class Program(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField()
    course = models.ManyToManyField(Course)


class Unit(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    program = models.ManyToManyField(Program)
