from django import forms

from .models import *


class CourseForm(forms.ModelForm):

    program = forms.ModelChoiceField(queryset=Program.objects.all().values_list('name', flat=True).order_by('name'),
                                     empty_label='Curso')

    class Meta:
        model = Course
        fields = ['name', 'group']
