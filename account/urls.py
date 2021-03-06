from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from account import views

urlpatterns = [
    path('', views.redirect_to_login_page),
    path('home', views.home, name='home'),
    path('accounts/login/', views.login, name='login'),
    path('accounts/logout/', views.logout, name='logout'),
    path('accounts/signupteacher/', views.signup_teacher, name='signup_teacher'),
    path('accounts/signupstudent/', views.signup_student, name='signup_student'),
    path('accounts/signuptype/', views.signup_type, name='signup_type'),
] + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
