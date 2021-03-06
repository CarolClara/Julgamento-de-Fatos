from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from core.views import JFBaseView
from .forms import GroupForm
from .models import Group


class GroupListView(JFBaseView, ListView):
    app_title = "Turmas"
    model = Group
    template_name = 'group_list.html'

    def get_queryset(self, **kwargs):
        return Group.objects.all().order_by('id')


class GroupCreateView(JFBaseView, CreateView):
    app_title = "Turmas"
    model = Group

    def get(self, request, *args, **kwargs):
        context = {'form': GroupForm()}
        return render(request, 'group_create.html', context)

    def post(self, request, *args, **kwargs):
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save()
            group.save()
            return HttpResponseRedirect(reverse_lazy('group_detail', args=[group.id]))
        return render(request, 'group_create.html', {'form': form})


class GroupUpdateView(JFBaseView, UpdateView):
    app_title = "Turmas"
    model = Group
    form_class = GroupForm
    template_name = 'group_update.html'

    def get_object(self, queryset=None):
        return Group.objects.get(id=self.kwargs['id'])


class GroupDetailView(JFBaseView, DetailView):
    app_title = "Turmas"
    model = Group
    template_name = 'group_detail.html'
    context_object_name = 'group'

    def get_object(self, queryset=None):
        return Group.objects.get(id=self.kwargs['id'])


class GroupDeleteView(LoginRequiredMixin, DeleteView):
    app_title = "Turmas"
    model = Group
    success_url = reverse_lazy('group_list')
    template_name = 'group_delete.html'

    def get_object(self, queryset=None):
        return Group.objects.get(id=self.kwargs['id'])
