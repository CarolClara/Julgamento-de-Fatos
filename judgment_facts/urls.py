from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from judgment_facts import views

urlpatterns = [
    path('judgment_facts/', views.JudgmentFactsListView.as_view(), name='judgment_facts'),
    path('judgment_facts/create/', views.JudgmentFactsCreateView.as_view(), name='judgement_facts_create'),
    path('judgment_facts/<id>/update', views.JudgmentFactsUpdateView.as_view(), name='judgment_facts_update'),
    path('judgment_facts/<id>/detail', views.JudgmentFactsDetailView.as_view(), name='judgment_facts_detail'),
    path('judgment_facts/<id>/delete', views.JudgmentFactsDeleteView.as_view(), name='judgment_facts_delete'),
] + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)