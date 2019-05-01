from django import forms

from account.models import Student
from .models import *


class JudgmentFactsForm(forms.ModelForm):

    class Meta:
        model = JudgmentFacts
        fields = ['name', 'team_length', 'fact_max_time', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'team_length': forms.IntegerField(attrs={'placeholder': 'Tamanho max. de membros por equipe'}),
            'fact_max_time': forms.IntegerField(attrs={'placeholder': u'Tamanho max. de exebição do fato'}),
            'status': forms.ChoiceField(attrs={'placeholder': 'Status'})
        }


class FactForm(forms.ModelForm):

    class Meta:
        model = Fact
        fields = ['order', 'statement', 'topic_group', 'correct_answer']
        CORRECT_ANSWER = Choices(
            (True, 'Verdadeiro'),
            (False, 'Falso'),
        )
        widgets = {
            'order': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'statement': forms.Textarea(attrs={'placeholder': 'Enunciado do fato'}),
            'topic_group': forms.IntegerField(attrs={'placeholder': u'Tópico da disciplina'}),
            'correct_answer': forms.ChoiceField(
                attrs={'placeholder': 'Resposta correta'}, choices=CORRECT_ANSWER, widget=forms.RadioSelect
            )
        }


class TeamFact(forms.ModelForm):

    class Meta:
        model = Team
        fields = ['name', 'member']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'member': forms.MultipleChoiceField(
                queryset=Student.objects.all().values_list('name', flat=True).exclude(pk__in=Team.objects.all()).order_by('name'),
                attrs={'placeholder': 'Membros'}
            )
        }
