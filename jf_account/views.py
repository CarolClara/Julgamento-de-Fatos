from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from jf_account.forms import TeacherForm, StudentForm
from .forms import LoginForm


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('registration/home.html'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Alguém tentou logar e falhou.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Login invalido")
    else:
        return render(request, 'registration/login.html', {})


def signup_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(request, 'base.html')
    else:
        form = TeacherForm()
        return render(request, "registration/signup_teacher.html", {'form': form})


def signup_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(request, 'base.html')
    else:
        form = StudentForm()
        return render(request, "registration/signup_student.html", {'form': form})
