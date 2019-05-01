from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .forms import GroupForm
from .models import Group


class GroupListView(ListView):
    model = Group
    template_name = 'group_list.html'

    def get_queryset(self, **kwargs):
        return Group.objects.all().order_by('id')


class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'group_create.html'


class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupForm


class GroupDetailView(DetailView):
    model = Group
    template_name = ''
    context_object_name = 'group'


class GroupDeleteView(DeleteView):
    model = Group
    success_url = reverse_lazy('group_list')
