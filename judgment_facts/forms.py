from django import forms

from account.models import Student
from .models import *


class JudgmentFactsForm(forms.ModelForm):

    class Meta:
        model = JudgmentFacts
        fields = ['name', 'team_length', 'fact_max_time', 'status']


class FactForm(forms.ModelForm):

    CORRECT_ANSWER = Choices(
        (True, 'Verdadeiro'),
        (False, 'Falso'),
    )
    correct_answer = forms.ChoiceField(choices=CORRECT_ANSWER, widget=forms.RadioSelect())

    class Meta:
        model = Fact
        fields = ['order', 'statement', 'topic_group', 'correct_answer']

    def save(self, commit=True, **kwargs):
        jf = JudgmentFacts.objects.get(id=kwargs['jf_id'])
        data = self.data
        return Fact.objects.create(
            order=data['order'], statement=data['statement'], topic_group=data['topic_group'],
            correct_answer=data['correct_answer'], judgment_facts=jf
        )


class TeamForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TeamForm, self).__init__(*args, **kwargs)
        self.fields['member'].queryset = Student.objects.all().exclude(pk__in=Team.objects.all()).order_by('user__name')

    class Meta:
        model = Team
        fields = ['name', 'member']
