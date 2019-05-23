from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from core.views import JFBaseView
from .forms import *
from .models import *


class JudgmentFactsListView(JFBaseView, ListView):
    app_title = "Julgamento de Fatos"
    model = JudgmentFacts
    template_name = 'jf_list.html'

    def get_queryset(self, **kwargs):
        return JudgmentFacts.objects.all().order_by('id')


class JudgmentFactsCreateView(JFBaseView, CreateView):
    app_title = "Julgamento de Fatos"
    model = JudgmentFacts

    def get(self, request, *args, **kwargs):
        context = {'form': JudgmentFactsForm()}
        return render(request, 'jf_create.html', context)

    def post(self, request, *args, **kwargs):
        form = JudgmentFactsForm(request.POST)
        if form.is_valid():
            jf = form.save()
            jf.save()
            return HttpResponseRedirect(reverse_lazy('fact_create', kwargs={'jf_id': jf.id}))
        return render(request, 'jf_create.html', {'form': form})


class JudgmentFactsUpdateView(JFBaseView, UpdateView):
    app_title = "Julgamento de Fatos"
    model = JudgmentFacts
    form_class = JudgmentFactsForm
    template_name = 'jf_update.html'


class JudgmentFactsDetailView(JFBaseView, DetailView):
    app_title = "Julgamento de Fatos"
    model = JudgmentFacts
    template_name = 'jf_detail.html'
    context_object_name = 'jf'

    def get_object(self, queryset=None):
        return JudgmentFacts.objects.get(id=self.kwargs['id'])


class JudgmentFactsDeleteView(JFBaseView, DeleteView):
    app_title = "Julgamento de Fatos"
    model = JudgmentFacts
    success_url = reverse_lazy('judgment_facts_list')
    template_name = 'jf_delete.html'


class FactListView(JFBaseView, ListView):
    app_title = "Fatos"
    model = Fact
    template_name = 'fact_list.html'

    def get_queryset(self, **kwargs):
        return Fact.objects.filter(judgment_facts__id=kwargs['jf_id']).order_by('id')

    def get_context_data(self, **kwargs):
        context = super(FactListView, self).get_context_data()
        context['id_jf'] = kwargs['id_jf']


class FactCreateView(JFBaseView, CreateView):
    app_title = "Fatos"
    model = Fact

    def get(self, request, *args, **kwargs):
        context = {'form': FactForm()}
        return render(request, 'fact_create.html', context)

    def post(self, request, *args, **kwargs):
        form = FactForm(request.POST, kwargs)
        if form.is_valid():
            fact = form.save()
            fact.save()
            return HttpResponseRedirect(reverse_lazy('fact_list', args=[fact.id]))
        return render(request, 'fact_create.html', {'form': form})


class FactUpdateView(JFBaseView, UpdateView):
    app_title = "Fatos"
    model = Fact
    form_class = FactForm
    template_name = 'fact_update.html'


class FactDeleteView(JFBaseView, DeleteView):
    app_title = "Fatos"
    model = Fact
    success_url = reverse_lazy('fact_list')
    template_name = 'fact_delete.html'


class TeamCreateView(JFBaseView, CreateView):
    app_title = "Equipes"
    model = Team

    def get(self, request, *args, **kwargs):
        context = {'form': TeamForm()}
        return render(request, 'team_create.html', context)

    def post(self, request, *args, **kwargs):
        form = FactForm(request.POST)
        if form.is_valid():
            team = form.save()
            team.save()
            return HttpResponseRedirect(reverse_lazy('team_detail', args=[team.id]))
        return render(request, 'team_create.html', {'form': form})


class TeamUpdateView(JFBaseView, UpdateView):
    app_title = "Equipes"
    model = Team
    form_class = TeamForm
    template_name = 'team_update.html'


class TeamDetailView(JFBaseView, DetailView):
    app_title = "Equipes"
    model = Team
    template_name = 'team_detail.html'
    context_object_name = 'team'

    def get_object(self, queryset=None):
        return Team.objects.get(id=self.kwargs['id'])


class TeamDeleteView(JFBaseView, DeleteView):
    app_title = "Equipes"
    model = Team
    success_url = reverse_lazy('judgment_facts_list')
    template_name = 'team_delete.html'
