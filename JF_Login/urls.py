from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from JF_Login import views

urlpatterns = [
    path('accounts/login', views.login_page, name='login'),
    path('accounts/signupteacher', views.signup_teacher, name='signup_teacher'),
    path('accounts/signupstudent', views.signup_student, name='signup_student'),
] + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
