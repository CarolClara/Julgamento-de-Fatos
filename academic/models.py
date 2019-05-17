from django.db import models
from django.urls import reverse

from account.models import Student


class Course(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, verbose_name='Nome')

    def __str__(self):
        return self.name


class Program(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, verbose_name='Nome')
    course = models.ManyToManyField(Course, verbose_name='Disciplina')

    def __str__(self):
        return self.name


class Unit(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, verbose_name='Nome', unique=True)
    program = models.ManyToManyField(Program, verbose_name='Curso')

    def __str__(self):
        return self.name


class Group(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, verbose_name='Nome')
    student = models.ManyToManyField(Student, verbose_name='Alunos')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Disciplina')
    program = models.ForeignKey(Program, on_delete=models.CASCADE, verbose_name='Curso')
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, verbose_name='Unidade')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        reverse('app:group_detail', kwargs={'id': self.id})
