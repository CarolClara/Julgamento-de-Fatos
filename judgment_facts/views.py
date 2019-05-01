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
            return HttpResponseRedirect(reverse_lazy('judgment_facts_detail', args=[jf.id]))
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
