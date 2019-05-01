from django import forms

from account.models import Student
from .models import *


class JudgmentFactsForm(forms.ModelForm):

    class Meta:
        model = JudgmentFacts
        fields = ['name', 'team_length', 'fact_max_time', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nome'}),
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
            'statement': forms.Textarea(attrs={'placeholder': 'Enunciado do fato'}),
            'topic_group': forms.TextInput(attrs={'placeholder': 'Tópico da disciplina'}),
            'correct_answer': forms.ChoiceField(choices=CORRECT_ANSWER, widget=forms.RadioSelect())
        }


class TeamFact(forms.ModelForm):

    member = forms.MultipleChoiceField(
        choices=Student.objects.values_list(
            'user__name', flat=True
        ).exclude(pk__in=Team.objects.all()).order_by('user__name')
    )

    class Meta:
        model = Team
        fields = ['name', 'member']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nome'})
        }
