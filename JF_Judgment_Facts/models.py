from django.db import models
from django.core.validators import MaxValueValidator

from model_utils.fields import StatusField
from model_utils import Choices

from JF_Login.models import Student


class Team(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    leader = models.ForeignKey(Student, on_delete=models.PROTECT, unique=True)
    member = models.ManyToManyField(Student)


class Fact(models.Model):

    id = models.AutoField(primary_key=True)
    order = models.PositiveIntegerField(validators=[MaxValueValidator(99)], unique=True)
    statement = models.CharField()
    topic_course = models.CharField()
    correct_answer = models.BooleanField()


class JudgmentFacts(models.Model):

    STATUS = Choices('CREATION', 'PREPARATION', 'EXECUTION', 'FINALIZED')

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    team_length = models.IntegerField(max_length=10)
    fact_max_time = models.TimeField()
    status = StatusField(choices_name='STATUS')
    fact = models.ManyToManyField(Fact)
    team = models.ManyToManyField(Team)
