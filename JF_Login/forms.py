from django import forms


class LoginForm(forms.Form):
    loginform = forms.CharField(label='Username', max_length=100)
    passoword = forms.CharField(label='Senha', max_length=32)