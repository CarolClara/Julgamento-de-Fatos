from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from jf_account.forms import TeacherForm, StudentForm
from .forms import LoginForm


def login_page(request):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return HttpResponseRedirect("/home.html")
    return render(request, 'registration/login.html', {'LoginForm': form})


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
