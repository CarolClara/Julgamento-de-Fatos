from django.db import models
from django.core.validators import MaxValueValidator

from model_utils.fields import StatusField
from model_utils import Choices


class Team(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    leader = models.OneToOneField('account.Student', on_delete=models.PROTECT, related_name='student_leader_set')
    member = models.ManyToManyField('account.Student', related_name='student_member_set')

    def __str__(self):
        return self.name


class JudgmentFacts(models.Model):

    CREATION = 1
    PREPARATION = 2
    EXECUTION = 3
    FINALIZED = 4

    STATUS = Choices(
        (CREATION, u'Em criação'),
        (PREPARATION, u'Em preparação'),
        (EXECUTION, u'Em execução'),
        (FINALIZED, u'Finalizado')
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    team_length = models.IntegerField()
    fact_max_time = models.TimeField()
    status = StatusField(choices_name='STATUS', default=CREATION)
    team = models.ManyToManyField(Team)

    def __str__(self):
        return self.name


class Fact(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.PositiveIntegerField(validators=[MaxValueValidator(99)], unique=True)
    statement = models.CharField(max_length=250)
    topic_group = models.CharField(max_length=250)
    correct_answer = models.BooleanField()
    judgment_facts = models.ForeignKey(JudgmentFacts, on_delete=models.CASCADE)

    def __str__(self):
        return self.statement


class TeamFact(models.Model):

    id = models.AutoField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    fact = models.ForeignKey(Fact, on_delete=models.PROTECT)
    team_answer = models.BooleanField()

    def __str__(self):
        return 'Equipe {} - Fato {}'.format(self.team, self.fact.id)
