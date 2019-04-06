from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from jf_account import views

urlpatterns = [
    path('accounts/login/', views.login_page, name='login'),
    path('accounts/signupteacher/', views.signup_teacher, name='signup_teacher'),
    path('accounts/signupstudent/', views.signup_student, name='signup_student'),
    path('accounts/signuptype/', views.signup_type, name='signup_type'),
] + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
