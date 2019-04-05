from django.db import models

from jf_judgment_facts.models import JudgmentFacts
from jf_account.models import Student


class Group(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    student = models.ManyToManyField(Student)
    judgment_facts = models.ManyToManyField(JudgmentFacts)


class GroupStudent(models.Model):

    id = models.AutoField(primary_key=True)
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)


class Course(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    group = models.ManyToManyField(Group)


class Program(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    course = models.ManyToManyField(Course)


class Unit(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, unique=True)
    program = models.ManyToManyField(Program)
