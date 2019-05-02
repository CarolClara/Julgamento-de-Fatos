from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .forms import *
from .models import *


class JudgmentFactsListView(ListView):
    model = JudgmentFacts
    template_name = 'jf_list.html'

    def get_queryset(self, **kwargs):
        return JudgmentFacts.objects.all().order_by('id')


class JudgmentFactsCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': JudgmentFactsForm()}
        return render(request, 'jf_create.html', context)

    def post(self, request, *args, **kwargs):
        form = JudgmentFactsForm(request.POST)
        if form.is_valid():
            jf = form.save()
            jf.save()
            return HttpResponseRedirect(reverse_lazy('fact_create', args=[jf.id]))
        return render(request, 'jf_create.html', {'form': form})


class JudgmentFactsUpdateView(UpdateView):
    model = JudgmentFacts
    form_class = JudgmentFactsForm
    template_name = 'jf_update.html'


class JudgmentFactsDetailView(DetailView):
    model = JudgmentFacts
    template_name = 'jf_detail.html'
    context_object_name = 'jf'

    def get_object(self, queryset=None):
        return JudgmentFacts.objects.get(id=self.kwargs['id'])


class JudgmentFactsDeleteView(DeleteView):
    model = JudgmentFacts
    success_url = reverse_lazy('judgment_facts_list')
    template_name = 'jf_delete.html'


class FactListView(ListView):
    model = Fact
    template_name = 'fact_list.html'

    def get_queryset(self, **kwargs):
        return Fact.objects.all().order_by('id')


class FactCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': FactForm()}
        return render(request, 'fact_create.html', context)

    def post(self, request, *args, **kwargs):
        form = FactForm(request.POST)
        if form.is_valid():
            fact = form.save()
            fact.save()
            return HttpResponseRedirect(reverse_lazy('fact_list', args=[fact.id]))
        return render(request, 'fact_create.html', {'form': form})


class FactUpdateView(UpdateView):
    model = Fact
    form_class = FactForm
    template_name = 'fact_update.html'


class FactDeleteView(DeleteView):
    model = Fact
    success_url = reverse_lazy('fact_list')
    template_name = 'fact_delete.html'


class TeamCreateView(CreateView):
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


class TeamUpdateView(UpdateView):
    model = Fact
    form_class = FactForm
    template_name = 'team_update.html'


class TeamDetailView(DetailView):
    model = Team
    template_name = 'team_detail.html'
    context_object_name = 'team'

    def get_object(self, queryset=None):
        return Team.objects.get(id=self.kwargs['id'])


class TeamDeleteView(DeleteView):
    model = Fact
    success_url = reverse_lazy('judgment_facts_list')
    template_name = 'team_delete.html'
