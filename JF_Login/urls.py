from django.urls import include, path
from JF_Login import views

urlpatterns = [
    #path('accounts/', views.login_page, name='login'),
    path('signupteacher', views.signup_teacher, name='signup_teacher'),
    path('signupstudent', views.signup_student, name='signup_teacher'),
]
