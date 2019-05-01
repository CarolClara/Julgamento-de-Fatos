from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .forms import *
from .models import *


class JudgmentFactsListView(ListView):
    model = JudgmentFacts

    def get_queryset(self, **kwargs):
        return JudgmentFacts.objects.all().order_by('id')


class JudgmentFactsCreateView(CreateView):
    model = JudgmentFacts
    form_class = JudgmentFactsForm


class JudgmentFactsUpdateView(UpdateView):
    model = JudgmentFacts
    form_class = JudgmentFactsForm


class JudgmentFactsDetailView(DetailView):
    model = JudgmentFacts
    template_name = ''
    context_object_name = 'group'


class GroupDeleteView(DeleteView):
    model = JudgmentFacts
    success_url = reverse_lazy('group_list')
