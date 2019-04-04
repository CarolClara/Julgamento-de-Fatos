from django.shortcuts import render, redirect

from JF_Login.forms import TeacherForm, StudentForm
from .forms import LoginForm


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        return ''
    else:
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})


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
