from django.contrib.auth import authenticate, login as login_django, logout as logout_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from account.forms import TeacherForm, StudentForm


@login_required
def home(request):
    return render(request, 'registration/home.html')


def login(request):
    if request.method == 'POST':

        form = AuthenticationForm(request=request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user and user.is_active:
                request.session['user_id'] = user.id
                login_django(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse("Nome de usuário ou senha estão incorretos")

    return render(request, 'registration/login.html', {'form': AuthenticationForm(request)})


def logout(request):
    try:
        del request.session['user_id']
        logout_django(request)
    except:
        pass
    return HttpResponseRedirect(reverse('login'))


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


def redirect_to_login_page(request):
    return HttpResponseRedirect(reverse('login'))
