import re

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

from academic.models import Program
from .models import *


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': u'Usuário'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Senha'})
        }


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['name', 'email', 'username', 'password']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'email': forms.EmailInput(attrs={'placeholder': 'E-mail'}),
            'username': forms.TextInput(attrs={'placeholder': u'Nome de usuário'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Senha'})
        }

    def save(self, commit=True):
        data = self.data
        return User.objects.create(
            name=data['name'], email=data['email'], username=data['username'],
            password=make_password(data['password'], None, 'md5'))

    def is_valid(self):
        username = self.data.get('username')
        password = self.data.get('password')

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
        return len(username) >= 5 and username.isalnum()


class TeacherForm(UserForm):

    def save(self, commit=True):
        user = UserForm.save(self)
        instance = Teacher.objects.create(user=user)

        return instance


class StudentForm(UserForm):

    program = forms.ModelChoiceField(
        queryset=Program.objects.all().values_list('name', flat=True).order_by('name'), empty_label=''
    )

    def save(self, commit=True):
        program = Program.objects.get(name=self.data.get('program'))
        user = UserForm.save(self)
        instance = Student.objects.create(user=user, program=program)

        return instance
