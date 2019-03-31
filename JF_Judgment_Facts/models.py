from django.db import models
from django.core.validators import MaxValueValidator

from model_utils.fields import StatusField
from model_utils import Choices


class Team(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    leader = models.ForeignKey('JF_Login.models.Student', on_delete=models.PROTECT, unique=True)
    member = models.ManyToManyField('JF_Login.models.Student', unique=True)


class Fact(models.Model):

    id = models.AutoField(primary_key=True)
    order = models.PositiveIntegerField(validators=[MaxValueValidator(99)], unique=True)
    statement = models.CharField()
    topic_course = models.CharField()
    correct_answer = models.BooleanField()


class TeamFact(models.Model):

    id = models.AutoField(primary_key=True)
    team_id = models.ForeignKey(Team.id, on_delete=models.PROTECT)
    fact_id = models.ForeignKey(Fact.id, on_delete=models.PROTECT)
    team_answer = models.BooleanField()


class JudgmentFacts(models.Model):

    CREATION = 1
    PREPARATION = 2
    EXECUTION = 3
    FINALIZED = 4

    STATUS = Choices(
        (CREATION, (u'Em criação')), (PREPARATION, (u'Em preparação')), (EXECUTION, (u'Em execução')), (FINALIZED, (u'Finalizado'))
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    team_length = models.IntegerField(max_length=10)
    fact_max_time = models.TimeField()
    status = StatusField(choices_name='STATUS')
    fact = models.ManyToManyField(Fact)
    team = models.ManyToManyField(Team)
