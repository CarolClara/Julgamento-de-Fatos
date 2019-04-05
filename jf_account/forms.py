import re

from django import forms

from jf_academic.models import Program
from .models import *


class LoginForm(forms.Form):
    loginform = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Senha', max_length=32)

    widgets = {
        'loginform': forms.TextInput(attrs={'placeholder': 'Nome'}),
        'password': forms.TextInput(attrs={'placeholder': 'Senha'})
    }


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['name', 'email', 'username', 'password']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'email': forms.EmailInput(attrs={'placeholder': 'E-mail'}),
            'username': forms.TextInput(attrs={'placeholder': 'Nome de usuário'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Senha'})
        }

    def is_valid(self):
        data = self.cleaned_data
        username = data['username']
        password = data['password']

        return self.username_is_valid(username) and self.password_is_valid(password)

    def password_is_valid(self, password):
        regex = re.compile('[A-Za-z ][A-Za-z0-9!@#$%^&*_ ][-/|}{=+§¬¢£³²¹~´`.:;]*$')
        if regex.search(password):
            temp = ''.join(char for char in password if char.isalnum())
            if temp.isalnum():
                return True
            return False
        if password.isalnum():
            return True

    def username_is_valid(self, username):
        if len(username) >= 5 and username.isalnum():
            return True
        return False


class TeacherForm(UserForm):

    def save(self, commit=True):
        user = UserForm.save(self)
        instance = Teacher.objects.create(user=user)

        return instance


class StudentForm(UserForm):

    program = forms.ModelChoiceField(queryset=Program.objects.all())

    def save(self, commit=True):
        user = UserForm.save(self)
        instance = Student.objects.create(user=user)

        return instance
