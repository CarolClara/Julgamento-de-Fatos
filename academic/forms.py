from django import forms

from .models import *


class GroupForm(forms.ModelForm):

    unit = forms.ModelChoiceField(
        queryset=Unit.objects.values_list('name', flat=True).order_by('name'), empty_label=''
    )
    program = forms.ModelChoiceField(
        queryset=Program.objects.values_list('name', flat=True).order_by('name'), empty_label=''
    )
    course = forms.ModelChoiceField(
        queryset=Course.objects.values_list('name', flat=True).order_by('name'), empty_label=''
    )

    class Meta:
        model = Group
        fields = ['name', 'unit', 'program', 'course']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nome'}),
        }
