from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from judgment_facts import views

urlpatterns = [
    path('judgment_facts/', views.JudgmentFactsListView.as_view(), name='judgment_facts_list'),
    path('judgment_facts/create/', views.JudgmentFactsCreateView.as_view(), name='judgement_facts_create'),
    path('judgment_facts/<id>/update', views.JudgmentFactsUpdateView.as_view(), name='judgment_facts_update'),
    path('judgment_facts/<id>/detail', views.JudgmentFactsDetailView.as_view(), name='judgment_facts_detail'),
    path('judgment_facts/<id>/delete', views.JudgmentFactsDeleteView.as_view(), name='judgment_facts_delete'),
    path('fact/', views.FactListView.as_view(), name='fact_list'),
    path('fact/create/', views.FactCreateView.as_view(), name='fact_create'),
    path('fact/<id>/update', views.FactUpdateView.as_view(), name='fact_update'),
    path('fact/<id>/delete', views.FactDeleteView.as_view(), name='fact_delete'),
    path('team/create/', views.TeamCreateView.as_view(), name='team_create'),
    path('team/<id>/update', views.TeamUpdateView.as_view(), name='team_update'),
    path('team/<id>/detail', views.TeamDetailView.as_view(), name='team_detail'),
    path('team/<id>/delete', views.TeamDeleteView.as_view(), name='team_delete'),
] + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
