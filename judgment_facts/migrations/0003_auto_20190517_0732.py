# Generated by Django 2.1.7 on 2019-05-17 10:32

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0007_auto_20190517_0732'),
        ('judgment_facts', '0002_auto_20190426_0717'),
    ]

    operations = [
        migrations.AddField(
            model_name='judgmentfacts',
            name='group',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='academic.Group', verbose_name='Turma'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fact',
            name='correct_answer',
            field=models.BooleanField(verbose_name='Resposta correta'),
        ),
        migrations.AlterField(
            model_name='fact',
            name='judgment_facts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='judgment_facts.JudgmentFacts', verbose_name='Julgamento de Fatos'),
        ),
        migrations.AlterField(
            model_name='fact',
            name='order',
            field=models.PositiveIntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(99)], verbose_name='Ordem'),
        ),
        migrations.AlterField(
            model_name='fact',
            name='statement',
            field=models.CharField(max_length=250, verbose_name='Enunciado'),
        ),
        migrations.AlterField(
            model_name='fact',
            name='topic_group',
            field=models.CharField(max_length=250, verbose_name='Tópico da disciplina'),
        ),
        migrations.AlterField(
            model_name='judgmentfacts',
            name='fact_max_time',
            field=models.TimeField(verbose_name='Tempo max. para exibir fatos'),
        ),
        migrations.AlterField(
            model_name='judgmentfacts',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='judgmentfacts',
            name='status',
            field=model_utils.fields.StatusField(choices=[(0, 'dummy')], default=1, max_length=100, no_check_for_status=True, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='judgmentfacts',
            name='team',
            field=models.ManyToManyField(to='judgment_facts.Team', verbose_name='Equipe'),
        ),
        migrations.AlterField(
            model_name='judgmentfacts',
            name='team_length',
            field=models.PositiveIntegerField(verbose_name='Tamanho max. das equipes'),
        ),
        migrations.AlterField(
            model_name='team',
            name='leader',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='student_leader_set', to='account.Student', verbose_name='Líder'),
        ),
        migrations.AlterField(
            model_name='team',
            name='member',
            field=models.ManyToManyField(related_name='student_member_set', to='account.Student', verbose_name='Membros'),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=60, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='teamfact',
            name='fact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='judgment_facts.Fact', verbose_name='Fato'),
        ),
        migrations.AlterField(
            model_name='teamfact',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='judgment_facts.Team', verbose_name='Time'),
        ),
        migrations.AlterField(
            model_name='teamfact',
            name='team_answer',
            field=models.BooleanField(verbose_name='Resposta do time'),
        ),
    ]
