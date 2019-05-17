from django.db import models
from django.core.validators import MaxValueValidator

from model_utils.fields import StatusField
from model_utils import Choices

from academic.models import Group


class Team(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Nome', max_length=60)
    leader = models.OneToOneField('account.Student', verbose_name=u'Líder', on_delete=models.PROTECT, related_name='student_leader_set')
    member = models.ManyToManyField('account.Student', verbose_name='Membros', related_name='student_member_set')

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
    name = models.CharField(verbose_name='Nome', max_length=30)
    team_length = models.PositiveIntegerField(verbose_name='Tamanho max. das equipes')
    fact_max_time = models.TimeField(verbose_name='Tempo max. para exibir fatos')
    status = StatusField(choices_name='STATUS', verbose_name='Status', default=CREATION)
    group = models.ForeignKey(Group, verbose_name='Turma', on_delete=models.CASCADE)
    team = models.ManyToManyField(Team, verbose_name='Equipe')

    def __str__(self):
        return self.name


class Fact(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.PositiveIntegerField(validators=[MaxValueValidator(99)], verbose_name='Ordem', unique=True)
    statement = models.CharField(max_length=250, verbose_name='Enunciado')
    topic_group = models.CharField(max_length=250, verbose_name=u'Tópico da disciplina')
    correct_answer = models.BooleanField(verbose_name='Resposta correta')
    judgment_facts = models.ForeignKey(JudgmentFacts, verbose_name='Julgamento de Fatos', on_delete=models.CASCADE)

    def __str__(self):
        return self.statement


class TeamFact(models.Model):

    id = models.AutoField(primary_key=True)
    team = models.ForeignKey(Team, verbose_name='Time', on_delete=models.PROTECT)
    fact = models.ForeignKey(Fact, verbose_name='Fato', on_delete=models.PROTECT)
    team_answer = models.BooleanField(verbose_name='Resposta do time')

    def __str__(self):
        return 'Equipe {} - Fato {}'.format(self.team, self.fact.id)
