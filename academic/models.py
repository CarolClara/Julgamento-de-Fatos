from django.db import models
from django.urls import reverse

from judgment_facts.models import JudgmentFacts
from account.models import Student


class Course(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)

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


class Group(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    student = models.ManyToManyField(Student)
    judgment_facts = models.ManyToManyField(JudgmentFacts, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        reverse('group_detail', kwargs={'slug': self.id})
