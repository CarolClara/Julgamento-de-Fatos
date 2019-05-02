from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from account.forms import TeacherForm, StudentForm
from .forms import LoginForm


def redirect_to_login_page(request):
    response = redirect('accounts/login')

    return response


def redirect_to_group_page(request):
    response = redirect('academic/')

    return response


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return render(request, 'registration/home.html')
        else:
            return HttpResponse("Dados informados são inválidos")
    else:
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})


def signup_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "registration/home.html")
    else:
        form = TeacherForm()
        return render(request, "registration/signup_teacher.html", {'form': form})


def signup_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "registration/home.html")
    else:
        form = StudentForm()
        return render(request, "registration/signup_student.html", {'form': form})


def signup_type(request):
    return render(request, "registration/signup_type.html")
