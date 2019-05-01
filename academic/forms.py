from django import forms
from django.db.models import Q

from .models import *


class GroupForm(forms.ModelForm):

    unit = forms.ModelChoiceField(
        queryset=Unit.objects.all().order_by('name'), empty_label='', to_field_name='name'
    )
    program = forms.ModelChoiceField(
        queryset=Program.objects.all().order_by('name'), empty_label='', to_field_name='name'
    )
    course = forms.ModelChoiceField(
        queryset=Course.objects.all().order_by('name'), empty_label='', to_field_name='name'
    )
    student = forms.MultipleChoiceField(
        choices=Student.objects.values_list('id', 'user__name').order_by('user__name')
    )

    class Meta:
        model = Group
        fields = ['name', 'unit', 'program', 'course', 'student']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nome'}),
        }
