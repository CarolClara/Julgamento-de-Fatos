from django.db import models

from judgment_facts.models import JudgmentFacts
from account.models import Student


class Group(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    student = models.ManyToManyField(Student)
    judgment_facts = models.ManyToManyField(JudgmentFacts)

    def __str__(self):
        return self.name


class Course(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    group = models.ManyToManyField(Group)

    def __str__(self):
        return self.name


class Program(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    course = models.ManyToManyField(Course)

    def __str__(self):
        return self.name


class Unit(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, unique=True)
    program = models.ManyToManyField(Program)

    def __str__(self):
        return self.name
