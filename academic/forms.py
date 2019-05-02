from django import forms

from .models import *


class GroupForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)
        self.fields['student'].queryset = Student.objects.all().order_by('user__name')

    unit = forms.ModelChoiceField(
        queryset=Unit.objects.all().order_by('name'), empty_label='', to_field_name='name'
    )
    program = forms.ModelChoiceField(
        queryset=Program.objects.all().order_by('name'), empty_label='', to_field_name='name'
    )
    course = forms.ModelChoiceField(
        queryset=Course.objects.all().order_by('name'), empty_label='', to_field_name='name'
    )

    class Meta:
        model = Group
        fields = ['name', 'unit', 'program', 'course', 'student']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nome'}),
        }
