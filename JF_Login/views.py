from django.shortcuts import render
from JF_Login.models import User
from JF_Login.serializers import LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponseRedirect
from .forms import LoginForm

class Login(APIView):

    def get(self, request, format=None):
        login = User.objects.all()
        serializer = LoginSerializer(login, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        return ''
    else:
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})