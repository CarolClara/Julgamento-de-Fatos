import re

from django import forms

from .models import *

class LoginForm(forms.Form):
    loginform = forms.CharField(label='Username', max_length=100)
    passoword = forms.CharField(label='Senha', max_length=32)


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['name', 'username', 'password', 'email']

    def is_valid(self):
        data = UserForm.cleaned_data
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

    class Meta:
        fields = ['program']

    def save(self, commit=True):
        user = UserForm.save(self)
        instance = Student.objects.create(user=user)

        return instance
