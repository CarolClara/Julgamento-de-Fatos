from django.urls import include, path
from rest_framework import routers
from JF_Login import views

router = routers.DefaultRouter()
router.register(r'login', views.Login)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
