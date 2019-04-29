from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from academic import views

urlpatterns = [
    path('academic/', views.GroupListView, name='group_list'),
    path('academic/create/', views.GroupCreateView, name='group_create'),
    path('academic/<slug:slug>/update', views.GroupUpdateView, name='group_update'),
    path('academic/<slug:slug>/delete', views.GroupDetailView, name='group_detail'),
] + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
