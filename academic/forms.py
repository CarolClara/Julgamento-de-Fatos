from django import forms

from .models import *


class GroupForm(forms.ModelForm):

    unit = forms.ModelChoiceField(
        queryset=Unit.objects.all().values_list('name', flat=True).order_by('name'), empty_label='', widget='Unidade')
    program = forms.ModelChoiceField(
        queryset=Program.objects.all().values_list('name', flat=True).order_by('name'), empty_label='', widget='Curso')

    class Meta:
        model = Group
        fields = ['name', 'unit', 'program', 'course']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'course': forms.ModelChoiceField(
                queryset=Course.objects.all().values_list('name', flat=True).order_by('name'),
                attrs={'placeholder': 'Disciplina'}
            )
        }
